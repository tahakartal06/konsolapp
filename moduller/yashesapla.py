def yashesaplam():
    import datetime

    dogumyili = int(input("Doğum yılınızı giriniz."))

    zaman1 = datetime.datetime.now().strftime("%Y")

    print(f"Yaşınız {int(zaman1)-dogumyili}dir.")
