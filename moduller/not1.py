def notm():
    print("Not değerlendirme programı")
    not1 = int(input("Ders puanın kaç?"))
    print(f"Dersinden {not1} puan almışsın.")

    if not1>100 or not1<0 :
        print("Girdiğiniz puan 0 ile 100 arasında olmalıdır.Lütfen tekrar deneyiniz.")
    else:
        if not1>90 : print("Harika")
        elif not1>50 and not1<90 :
            print("Geçtin")
        elif not1<50 : print("kaldın")

