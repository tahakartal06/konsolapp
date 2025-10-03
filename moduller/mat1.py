
    import random
    print(" *** Matematik alıştırmaları programı ***")
    devam = "evet"
    bilinen = 0
    while devam.upper() in ["EVET" , "E" , "EVT"]:
        s1 = random.randint(1,100)
        s2 = random.randint(1,100)
        cevap = int(input(f"{s1} + {s2} = ?"))
        if cevap == s1+s2:
            bilinen += 1
            print("Bildin. \nPuanın:", bilinen*10)
        else : print("yanlış cevap")
        devam = input("Devam edicek misiniz?")
    else : print(f"Oyun {bilinen*10} puan ile bitti.Tebrikler")