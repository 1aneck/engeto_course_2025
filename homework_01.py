'''
2/6 Zapiš pozdrav a odděl jej pomocnou proměnnou
VITEJTE U NASI APLIKACE DESTINATIO!
===================================

3/6 Vypiš nabídku cílových destinací a odděl ji pomocnou proměnnou
VITEJTE U NASI APLIKACE DESTINATIO!
===================================
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180

4/6 Dovol uživateli zadat 'destinace', 'cele_jmeno', 'email', 'rok_narozeni' a doplň oddělovač
<predchozi_ukoly>
===================================
CISLO DESTINACE: 1
JMENO: Matous
PRIJMENI: Holinka
EMAIL: matous@matous.cz
===================================

5/6 Zkus propojit stávající datový typ "mesta" a "destinace"
<predchozi_ukoly>
===================================
CISLO DESTINACE: 2
===================================
Viden
200
===================================

6/6 Vypiš tyto informace pro objednávajícího uživatele
 - Kdo si objednal,
 - kam cestuje a za kolik,
 - kam mu přijde lístek.
VITEJTE U NASI APLIKACE DESTINATIO!
===================================
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
===================================
CISLO DESTINACE: 2
JMENO: Matous
PRIJMENI: Holinka
EMAIL: matous@matous.cz
===================================
DEKUJI, Matous ZA OBJEDNAVKU,
CIL. DESTINACE: Viden, CENA JIZDNEHO: 200,
NA TVUJ MAIL matous@matous.cz JSME TI POSLALI LISTEK.
===================================
'''

# 2/6
greetings = "VITEJTE U NASI APLIKACE DESTINATIO\n"
article_separator = "=" * len(greetings)
main_header = greetings + article_separator
print(main_header)

# 3/6
our_offer = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
print(our_offer)
print(article_separator)

# 4/6
full_name = input("Insert your full name: ")
date_of_birth = input("Insert your date of birth: ")
email_address = input("Insert your e-mail: ")
destination_number = input("Insert the destination number: ")
print(article_separator)

# 5/6
destination_list = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
price_list = [150, 200, 120, 120, 100, 180]
selected_destination = destination_list[int(destination_number) - 1] 
selected_destination_price = price_list[int(destination_number) - 1]
#print("Your order:\nDestination - " + selected_destination + "\nPrice: " + str(selected_destination_price) + ",-\n" + article_separator)

# 6/6
print(f"""Welcome on board, {full_name}!
Your trip to {selected_destination} for {selected_destination_price},- has been booked.
We have sent all important information to your email address - {email_address}.
Team DESTINATIO
""")