import pytest

import lineup

import bs4


@pytest.fixture
def arctangent_lineup_page():
    return "test/data/LINE-UP – ArcTanGent.html"


def test_find_artists():
    response = lineup.find_artists(
        file="test/data/LINE-UP – ArcTanGent.html",
        find_all="h2",
        class_="grid-title",
    )

    assert isinstance(response, bs4.element.ResultSet)
    assert len(response) == 117
