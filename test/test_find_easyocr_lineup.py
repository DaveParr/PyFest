import lineup

def test_find_easyocr_lineup():
    response = lineup.find_easyocr_lineup()
    assert response == "Chun is Great"