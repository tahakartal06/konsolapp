def alanvecevrem():
    print("╔"+"═"*30+"╗")
    print("║         Alan ve Çevre        ║")
    print("║                              ║")
    print("║        1-Alan ve Çevre(k)    ║")
    print("║        2-Alan ve Çevre(d)    ║")
    print("║                              ║")
    print("║                              ║")
    print("║                              ║")
    print("║    Lütfen seçim yapınız :    ║")
    print("╚"+"═"*30+"╝")
    secim = input()
    if secim == "1" or secim == "k":
        import moduller.karealan
        moduller.karealanproje()
    if secim == "2" or secim == "d":
        import moduller.dikalancevre
        moduller.dikalancevre()
if __name__ == "__main__":
    alanvecevrem()
