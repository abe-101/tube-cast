import pytest
from tube.youtube_dl import download_youtube_thumbnail, download_youtube_video


def test_download_youtube_video(capsys):
    video_id = "123d"
    download_youtube_video(video_id)
    captured = capsys.readouterr()
    assert (
        captured.err
        == f"ERROR: [youtube:truncated_id] {video_id}: Incomplete YouTube ID {video_id}. URL https://www.youtube.com/watch?v={video_id} looks truncated.\n"
    )


def test_download_youtube_thumbnail(capsys):
    video_id = "JCmu4"
    download_youtube_thumbnail(video_id)
    captured = capsys.readouterr()
    assert (
        captured.err
        == f"ERROR: [youtube:truncated_id] {video_id}: Incomplete YouTube ID {video_id}. URL https://www.youtube.com/watch?v={video_id} looks truncated.\n"
    )
