def yazituram():
    import random
    
    gir = input("Yazımı Turamı")
    yazitura = random.randint(1, 2)

    if yazitura == 1:
        tutulan = "yazı" 
        print("Yazı")
    else:
        tutulan = "tura"
        print("Tura")

    if  gir.upper() == tutulan.upper():
        print("Bildin")

    else:
        print("Bilemedin")
