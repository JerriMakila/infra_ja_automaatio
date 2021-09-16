import postinumerot

TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}


def test_onko_postinumeroita_kaksi():
    testi_data = TOIMIPAIKAT
    tulos = postinumerot.ryhmittele_toimipaikoittain(testi_data)

    assert len(tulos["KIURUVESI"]) == 2


def test_onko_postinumeroita_yksi():
    testi_data = TOIMIPAIKAT
    tulos = postinumerot.ryhmittele_toimipaikoittain(testi_data)

    assert len(tulos["JUUPAJOKI"]) == 1


def test_onko_avaimia_kolme():
    testi_data = TOIMIPAIKAT
    tulos = postinumerot.ryhmittele_toimipaikoittain(testi_data)

    assert len(tulos) == 3


def test_loytyyko_korvatunturi_http_kutsu():
    haettava_toimipaikka = "kOrVaTuNtUrI"
    tulos = postinumerot.printtaa_numerot(haettava_toimipaikka)

    assert tulos == 'Postinumerot: 99999'


def test_palauttaako_toimipaikkaa_ei_loytynyt_http_kutsu():
    haettava_toimipaikka = "ei ole olemassa"
    tulos = postinumerot.printtaa_numerot(haettava_toimipaikka)

    assert tulos == 'Toimipaikkaa ei löytynyt'


def test_onko_kiuruvedella_kaksi_numeroa_testidatassa(mocker):
    testi_data = TOIMIPAIKAT
    mocker.patch('http_pyynto.hae_postinumerot', return_value=testi_data)
    tulos = postinumerot.printtaa_numerot("kiuruvesi")

    assert tulos == "Postinumerot: 74700, 74701"


def test_onko_juupajoella_yksi_numero_testidatassa(mocker):
    testi_data = TOIMIPAIKAT
    mocker.patch('http_pyynto.hae_postinumerot', return_value=testi_data)
    tulos = postinumerot.printtaa_numerot("juupajoki")

    assert tulos == "Postinumerot: 35540"


def test_palauttaako_toimipaikkaa_ei_loytynyt_oma_data(mocker):
    testi_data = TOIMIPAIKAT
    mocker.patch('http_pyynto.hae_postinumerot', return_value=testi_data)
    tulos = postinumerot.printtaa_numerot("ei ole olemassa")

    assert tulos == "Toimipaikkaa ei löytynyt"
