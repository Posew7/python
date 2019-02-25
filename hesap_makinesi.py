def topla(a,b):
    c = a + b
    print(a,"+",b,"=",c,"\n\n\n")

def cikar(a,b):
    c = a - b
    print(a,"-",b,"=",c,"\n\n\n")

def carp(a,b):
    c = a * b
    print(a,"*",b,"=",c,"\n\n\n")

def bol(a,b):
    c = a / b
    print(a,"/",b,"=",c,"\n\n\n")

def main():
    while(True):
        a = int(input("birinci sayıyı giriniz : \n"))
        b = int(input("ikinci sayıyı giriniz : \n"))
        islem = input("yapmak istediğiniz işlemi giriniz  + - * /  : \n")
        if (islem == "+"):
            topla(a,b)
        elif (islem == "-"):
            cikar(a,b)
        elif (islem == "*"):
            carp(a,b)
        elif (islem == "/"):
            bol(a,b)
        else:
            print("yanlış bir giriş yaptınız\n\n\n")

main()