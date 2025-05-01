"""
Vytvoř takový podmínkový zápis, který bude reagovat na nesprávně zadaná hesla (viz. příklad níže):
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

heslo = heslo_6
"""

new_password = input("Create a strong password: ")
if new_password == "":
    print("FAILED - your password cannot be empty!")
elif len(new_password) < 8:
    print("FAILED - your password is too short!")
elif new_password.isnumeric() is True:
    print("FAILED - Your password must contain digits and letters!")
elif new_password[0].isnumeric() is True:
    print("FAILED - Your password must not start with digits!")
else:
    print("OK - Your password has been created")