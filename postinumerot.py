import http_pyynto


def printtaa_numerot(toimipaikka):
    haettava = toimipaikka.strip().upper().replace("-", "").replace(" ", "")
    postinumerot = http_pyynto.hae_postinumerot()
    toimipaikat = ryhmittele_toimipaikoittain(postinumerot)

    if haettava in toimipaikat:
        toimipaikat[haettava].sort()
        loydetyt_str = ', '.join(toimipaikat[haettava])
        return 'Postinumerot: ' + loydetyt_str
    else:
        return 'Toimipaikkaa ei löytynyt'


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        korjattu_nimi = nimi.replace(" ", "").replace("-", "")
        if korjattu_nimi not in paikat:
            paikat[korjattu_nimi] = []

        paikat[korjattu_nimi].append(numero)

    return paikat


def main():
    toimipaikka = input('Kirjoita postitoimipaikka: ')
    print(printtaa_numerot(toimipaikka))


if __name__ == '__main__':
    main()
