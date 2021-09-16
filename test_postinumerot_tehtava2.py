import postinumerot

TOIMIPAIKAT = {
    "44884": "SMART POST",
    "00000": "SMART-POST",
    "74704": "SMARTPOST",
    "40934": "SMART POST",
    "00001": "SMART-POST",
    "28204": "SMARTPOST",
    "65374": "SMART POST",
    "00002": "SMART-POST",
    "03604": "SMARTPOST",
    "07114": "SMART POST",
    "00003": "SMART-POST",
    "96204": "SMARTPOST",
    "00004": "TESTI-PAIKKA",
    "00005": "TESTI PAIKKA",
    "00006": "TESTIPAIKKA"
}


def test_onko_avaimia_kaksi():
    testi_data = TOIMIPAIKAT
    tulos = postinumerot.ryhmittele_toimipaikoittain(testi_data)

    assert len(tulos) == 2


def test_onko_postinumeroita_kaksitoista():
    testi_data = TOIMIPAIKAT
    tulos = postinumerot.ryhmittele_toimipaikoittain(testi_data)

    assert len(tulos["SMARTPOST"]) == 12
