import lineup
import pytest

@pytest.fixture
def slamdunk2016_poster():
    return "test/data/Slam-Dunk-Festival-2016-March-Poster.jpeg"

def test_find_easyocr_lineup(slamdunk2016_poster):
    response = lineup.find_easyocr_lineup(slamdunk2016_poster)
    assert isinstance(response, list)
    assert len(response)>50
