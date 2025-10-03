def dikalancevre():
    kisakenar = int(input("Kenar uzunluğu giriniz:"))
    uzunkenar = int(input("Kenar uzunluğu giriniz:"))

    cevre = (kisakenar + uzunkenar)*2
    alan = (kisakenar * uzunkenar)
    print(f"Diktörtgenin çevresi {cevre}")
    print(f"Dikdörtgenin alanı {alan}")

if __name__ == "__main__":
    dikalancevre()