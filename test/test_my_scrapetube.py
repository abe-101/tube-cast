import pytest
from tube.my_scrapetube import return_channel, return_playlist


def test_return_channel():
    with pytest.raises(SystemExit) as e:
        return_channel("123")
    assert e.type == SystemExit
    assert e.value.code == "Invalid channel id"


def test_return_playlist():
    with pytest.raises(SystemExit) as e:
        return_playlist("232")
    assert e.type == SystemExit
    assert e.value.code == "Invalid playlist id"


if __name__ == "__main__":
    test_exit()
