def oyunlarm():
    print("╔"+"═"*30+"╗")
    print("║            Oyunlar           ║")
    print("║                              ║")
    print("║        1-Yılan               ║")
    print("║        2-Matematik           ║")
    print("║        3-Taşkağıtmakas       ║")
    print("║                              ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :)   ║")
    print("╚"+"═"*30+"╝")
    secim = input()

    if secim == "1":
        import moduller.yılanoyunu
        moduller.yılanoyunu.yılanoyunum()
    if secim == "2":
        import moduller.mat1
        moduller.mat1.mat1m()
    if secim == "3":
        import moduller.taskagıtmakas
        moduller.taskagıtmakas.taskagıtmakasm()

