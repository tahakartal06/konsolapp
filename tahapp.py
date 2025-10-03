def tahapp():

    print("╔"+"═"*30+"╗")
    print("║           Ana sayfa          ║")
    print("║                              ║")
    print("║        1-Hesap Makinesi      ║")
    print("║        2-Uygulamalar         ║")
    print("║        3-Alan Hesaplama      ║")
    print("║        4-Oyunlar             ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :)   ║")
    print("╚"+"═"*30+"╝")
    secim = input()
    if secim == "1":
        import modullersayfa.hesapmakinesi
        modullersayfa.hesapmakinesi.hesapmakinesim()
    if secim == "2":
        import modullersayfa.uygulamalar
        modullersayfa.uygulamalar.uygulamalarm()
    if secim == "3":
        import modullersayfa.alanvecevre
        modullersayfa.alanvecevre.alanvecevrem()
    if secim == "4":
        import modullersayfa.oyunlar
        modullersayfa.oyunlar.oyunlarm()
    tahapp()

tahapp()


