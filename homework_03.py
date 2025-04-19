"""
sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62

film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}

film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}

film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}

#1 sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
 .. klíčem bude jméno filmu a samotný slovník následuje
 .. jako hodnota.

 #2 Výpis pro uživatele
                VÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!               
==============================================================
        dostupné filmy | detaily filmu | doporuč film         
==============================================================

#3 Zobraz mi dostupné filmy
                       Dostupné filmy:                        
==============================================================
Shawshank Redemption, The Godfather, The Dark Knight
==============================================================

#4 Zobraz detaily o filmu
Detaily filmu: 
==============================================================
{'jmeno': 'The Dark Knight', 'rating': '90/100', 'rok': 2008, 'reziser': 'Christopher Nolan', 'stopaz': 152}
==============================================================

#5 Zobraz seznam režisérů
Všichni režiséři:
==============================================================
{'Frank Darabont', 'Christopher Nolan', 'Francis Ford Coppola'}
==============================================================
"""