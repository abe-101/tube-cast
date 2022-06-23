import asyncio
import os
from pyppeteer import launch

def convert_youtube_to_podcast(youtube_id: str) -> bool:
    """
    Given a YouTube video ID it will create a Podcast on Anchor.fm
    """
    email = os.getenv('ANCHOR_EMAIL')
    password = os.getenv('ANCHOR_PASSWORD')
    thumbnailMode = os.getenv('LOAD_THUMBNAIL', 'false')
    urlDescription = os.getenv('URL_IN_DESCRIPTION', 'false')
    
    UPLOAD_TIMEOUT=60 * 5 * 1000

    url = 'https://www.youtube.com/watch?v=' + youtube_id

    episode = {'title': 'testing title', 'description': 'testing description'}
    
    # Draft mode
    draftMode = os.getenv('LOAD_THUMBNAIL', 'false')
    saveDraftOrPublishButtonXPath = '//button[text()="Save as draft"]' if draftMode == 'true' else '//button/div[text()="Publish now"]'
    
    # Is Explicit
    isExplicit = os.getenv('IS_EXPLICIT', 'false')
    selectorForExplicitContentLabel = 'label[for="podcastEpisodeIsExplicit-true"]' if isExplicit == 'true' else 'label[for="podcastEpisodeIsExplicit-false"]'
    
    
    
    async def Lauch():
        print("Launching puppeteer")
        browser = await launch(
                args=['--no-sandbox'],
                headless=False)
        page = await browser.newPage()
    
        navigationPromise = asyncio.ensure_future(page.waitForNavigation())
    
        await page.goto('https://anchor.fm/dashboard/episode/new')
    
        await page.setViewport({ 'width': 1600, 'height': 789 })
        await navigationPromise
    
        print("Trying to log in")
        await page.type('#email', email)
        await page.type('#password', password)
        await page.click('button[type=submit]')
        await navigationPromise
        print("Logged in")
    
        await page.waitForSelector('input[type=file]')
        print("Uploading audio file")
        inputFile = await page.J('input[type=file]')
        await inputFile.uploadFile('/home/thinkpad/repos/youtube-to-anchorfm/episode.mp3')
        #await inputFile.uploadFile(outputFile)
    
        print("Waiting for upload to finish")
        await page.waitFor(25 * 1000)
    
        await page.waitForXPath('//div[contains(text(),"Save")]/parent::button[not(boolean(@disabled))]', timeout=UPLOAD_TIMEOUT)
        [saveButton] = await page.Jx('//div[contains(text(),"Save")]/parent::button[not(boolean(@disabled))]')
        await saveButton.click()
        await navigationPromise
    
        print("-- Adding title")
        await page.waitForSelector('#title', visible=True)
        # Wait some time so any field refresh doesn't mess up with our input
        await page.waitFor(2000)
        await page.type('#title', episode['title'])
    
        print("-- Adding description")
        await page.waitForSelector('div[role="textbox"]', visible=True )
        await page.type('div[role="textbox"]', episode['description'])
    
        print("-- Selecting content type")
        await page.waitForSelector(selectorForExplicitContentLabel, visible=True)
        contentTypeLabel = await page.J(selectorForExplicitContentLabel)
        await contentTypeLabel.click()
    
        if (thumbnailMode != 'false'):
            print("-- Uploading episode art")
            await page.waitForSelector('input[type=file][accept="image/*"]')
            inputEpisodeArt = await page.J('input[type=file][accept="image/*"]')
            await inputEpisodeArt.uploadFile('/home/thinkpad/repos/youtube-to-anchorfm/thumbnail.jpg')
    
            print("-- Saving uploaded episode art")
            await page.waitForXPath('//button/div[text()="Save"]')
            [saveEpisodeArtButton] = await page.Jx('//button/div[text()="Save"]')
            await saveEpisodeArtButton.click()
            await page.waitForXPath('//div[@aria-label="image uploader"]', hidden=True, timeout=UPLOAD_TIMEOUT)
      
    
        print("-- Publishing")
        #await page.click(saveDraftOrPublishButtonXPath)
        button = await page.Jx(saveDraftOrPublishButtonXPath)
        if button:
            await button[0].click()
        else:
            await page.click('.styles__button___2oNPe.styles__purple___2u-0h.css-39f635')
        
    
        await navigationPromise
        await browser.close()
    
    #asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(Lauch())
convert_youtube_to_podcast('sds') 

THUMBNAIL_FORMAT = "jpg"
outputFile = 'episode.mp3'
