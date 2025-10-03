#Hesap Makinesi

def bilgial():
    s1 = int(input("1.Sayıyı Giriniz:"))
    s2 = int(input("2.Sayıyı Giriniz:"))
    return [s1,s2]
    # islem = input("İsleminiz Nedir(+,-,*,/)?")

    # if islem == "+" : print("Sonuç:", topla(s1,s2))
    # if islem == "*" : print("Sonuç:", carp(s1,s2))
    # if islem == "-" : print("Sonuç:", cikar(s1,s2))
    # if islem == "/" : print("Sonuç:", böl(s1,s2))

def topla():
    a = bilgial()
    print("Sonuç:",a[0]+ a[1])
    
def carp():
    a = bilgial()
    print("Sonuç:",a[0]* a[1])
    
def cikar():
     a = bilgial()
     print("Sonuç:",a[0]- a[1])

def böl():
     a = bilgial()
     print("Sonuç:",a[0]/ a[1])
    


