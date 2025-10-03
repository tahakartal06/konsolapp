import random

oyun_resimleri = ['''taş:
    _______
---'   ____
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''kağıt:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''makas:
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

devam = "evet"

while devam.lower() == "evet":
    insan_secimi = int(input('''Taş, kağıt, makas? "Taş" seçmek için "0", "kağıt" seçmek için "1" ve "makas" seçmek için "2" rakamına basın...\n'''))

    if 0 <= insan_secimi <= 2:
        print("Seçiminiz...")
        print(oyun_resimleri[insan_secimi])

        bilgisayar_secimi = random.randint(0, 2)
        print("Bilgisayar seçiyor...")
        print(oyun_resimleri[bilgisayar_secimi])

        if insan_secimi == 0 and bilgisayar_secimi == 2:
            print("Kazandınız!")
        elif bilgisayar_secimi == 0 and insan_secimi == 2:
            print("Kaybettiniz!")
        elif bilgisayar_secimi > insan_secimi:
            print("Kaybettiniz")
        elif insan_secimi > bilgisayar_secimi:
            print("Kazandınız!")
        elif bilgisayar_secimi == insan_secimi:
            print("Berabere kaldınız!")
    else:
        print("Geçersiz değer girdiniz...")

    devam = input("Tekrar oynamak ister misiniz? (evet/hayır): ")