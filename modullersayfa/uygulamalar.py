def uygulamalarm():
    print("╔"+"═"*30+"╗")
    print("║          Uygulamalar         ║")
    print("║                              ║")
    print("║      1-Pozitif Negatif       ║")
    print("║      2-Yazı Tura             ║")
    print("║      3-Yaş hesapla           ║")
    print("║      4-Geçtin Kaldın         ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :)   ║")
    print("╚"+"═"*30+"╝")
    secim = input()
    
    if secim in ["1","p","P"]:
        import moduller.pozneg
        moduller.pozneg.poznegh()
    if secim in ["2","y","E"]:
        import moduller.yazitura
        moduller.yazitura.yazituram()
    if secim in ["3","y","Y"]:
        import moduller.yashesapla
        moduller.yashesapla.yashesaplam()
    if secim in ["4","g","G"]:
        import moduller.not1
        moduller.not1.notm()



    

