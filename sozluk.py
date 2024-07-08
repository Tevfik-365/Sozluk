meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "MİNECRFT" : "Zanaat bana ait",
            'ROLEPLAY' : 'Rol yapmak',
            'EZ' : 'Rakibi aşağılamak',
            'AFK' : 'Oyun başladığında oyuna mola vermek'
             }
kelime = input("kelimeleri girin")
if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print('kelime listede yok')
