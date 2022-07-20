import asyncio
import os

from src.validate_id import valid_id
from pyppeteer import launch
from src.youtube_dl import download_youtube_thumbnail, download_youtube_video


def convert_youtube_to_podcast(
    youtube_ids: list,
    *,
    draft_mode=True,
    thumbnail_mode=True,
    url_in_description=True,
    is_explicit=False,
    headless_mode=True,
) -> dict:
    parameters = {
        "draft_mode": draft_mode,
        "thumbnail_mode": thumbnail_mode,
        "url_in_description": url_in_description,
        "is_explicit": is_explicit,
        "headless_mode": headless_mode,
    }

    results = []
    if len(youtube_ids) > 9:
        print("You are attempting to process more than 10 videos")
        print("This may take a long time")
        ans = input("Would you like to proceed? (YES/NO)\n")
        if ans != "YES":
            exit()
    for id in youtube_ids:
        if not valid_id(id):
            print(f"Video ID: {id} is not valid -- Skipping")
            results.append((id, "skipped"))
            continue
        if _convert_youtube_to_podcast(id, **parameters):
            results.append((id, "a success"))
        else:
            results.append((id, "a failure"))
    print("\n\n================ Results ================\n")
    for result in results:
        print(f"Video ID: {result[0]:11} was {result[1]}")


def _convert_youtube_to_podcast(
    youtube_id: str,
    *,
    draft_mode=True,
    thumbnail_mode=True,
    url_in_description=True,
    is_explicit=False,
    headless_mode=True,
) -> bool:
    """
    Given a YouTube video ID it will create a Podcast on Anchor.fm
    """
    email = os.getenv("ANCHOR_EMAIL")
    password = os.getenv("ANCHOR_PASSWORD")

    UPLOAD_TIMEOUT = 60 * 5 * 1000

    # Thumbnail Mode
    if thumbnail_mode is True:
        thumbnail_image_file_name = download_youtube_thumbnail(youtube_id)

    # Download YouTube video and retrieve metadata
    episode_info = download_youtube_video(youtube_id)

    # Append URL to description
    if url_in_description is True:
        episode_info["description"] = (
            episode_info["description"]
            + "\nhttps://www.youtube.com/watch?v="
            + youtube_id
        )

    # Draft mode
    saveDraftOrPublishButtonXPath = (
        '//button[text()="Save as draft"]'
        if draft_mode is True
        else '//button/div[text()="Publish now"]'
    )

    # Is Explicit
    selectorForExplicitContentLabel = (
        'label[for="podcastEpisodeIsExplicit-true"]'
        if is_explicit is True
        else 'label[for="podcastEpisodeIsExplicit-false"]'
    )

    async def Lauch():
        print("Launching pyppeteer")
        browser = await launch(args=["--no-sandbox"], headless=headless_mode)
        page = await browser.newPage()

        navigationPromise = asyncio.ensure_future(page.waitForNavigation())

        await page.goto("https://anchor.fm/dashboard/episode/new")

        await page.setViewport({"width": 1600, "height": 789})
        await navigationPromise

        print("Trying to log in")
        await page.type("#email", email)
        await page.type("#password", password)
        await page.click("button[type=submit]")
        await navigationPromise
        print("Logged in")

        await page.waitForSelector("input[type=file]")
        print("Uploading audio file")
        inputFile = await page.J("input[type=file]")
        await inputFile.uploadFile(episode_info["file_name"])

        await page.waitForXPath('//button[text()="Audio episode"]')
        [audioEpisodeButton] = await page.Jx('//button[text()="Audio episode"]')
        await audioEpisodeButton.click()

        print("Waiting for upload to finish")
        await page.waitFor(25 * 1000)

        await page.waitForXPath(
            '//div[contains(text(),"Save")]/parent::button[not(boolean(@disabled))]',
            timeout=UPLOAD_TIMEOUT,
        )
        [saveButton] = await page.Jx(
            '//div[contains(text(),"Save")]/parent::button[not(boolean(@disabled))]'
        )
        await saveButton.click()
        await navigationPromise

        print("-- Adding title")
        await page.waitForSelector("#title", visible=True)
        await page.waitFor(2000)
        await page.type("#title", episode_info["title"])

        print("-- Adding description")
        await page.waitForSelector('div[role="textbox"]', visible=True)
        await page.type('div[role="textbox"]', episode_info["description"])

        print("-- Selecting content type")
        await page.waitForSelector(selectorForExplicitContentLabel, visible=True)
        contentTypeLabel = await page.J(selectorForExplicitContentLabel)
        await contentTypeLabel.click()

        if thumbnail_mode is True:
            print("-- Uploading episode art")
            await page.waitForSelector('input[type=file][accept="image/*"]')
            inputEpisodeArt = await page.J('input[type=file][accept="image/*"]')
            await inputEpisodeArt.uploadFile(thumbnail_image_file_name)

            print("-- Saving uploaded episode art")
            await page.waitForXPath('//button/div[text()="Save"]')
            [saveEpisodeArtButton] = await page.Jx('//button/div[text()="Save"]')
            await saveEpisodeArtButton.click()
            await page.waitForXPath(
                '//div[@aria-label="image uploader"]',
                hidden=True,
                timeout=UPLOAD_TIMEOUT,
            )

        print("-- Publishing")
        button = await page.Jx(saveDraftOrPublishButtonXPath)
        if button:
            await button[0].click()
        else:
            await page.click(
                ".styles__button___2oNPe.styles__purple___2u-0h.css-39f635"
            )

        await navigationPromise
        await browser.close()

    asyncio.run(Lauch())

    # Remove downloaded Thumbnail image file
    if thumbnail_mode is True:
        if os.path.isfile(thumbnail_image_file_name):
            os.remove(thumbnail_image_file_name)

    # Remove downloaded downloaded audio file
    if os.path.isfile(episode_info["file_name"]):
        os.remove(episode_info["file_name"])
    return True
