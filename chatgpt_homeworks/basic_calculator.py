

def toplama(num_1,num_2):
    sonuç = int(num_1) + int (num_2) 
    print(sonuç)

def çikarma(num_1,num_2):
    sonuç = int(num_1) - int (num_2) 
    print(sonuç)

def çarpma(num_1,num_2):
    sonuç = int(num_1) * int (num_2) 
    print(sonuç)

def bölme(num_1,num_2):
    sonuç = int(num_1) / int (num_2) 
    print(sonuç)
 
 

def main():
    while True:
        num_1 = input("1.sayiyi giriniz: ")
        num_2 = input("2.sayiyi giriniz: ")
        işlem = input("İşlem seçiniz(toplama,çikarma,çarpma,bölme)veya çikiş yaz:")

        if işlem=="toplama":
            toplama(num_1,num_2)
        elif işlem=="çikarma":
            çikarma(num_1,num_2)
        elif işlem=="çarpma":
            çarpma(num_1,num_2)
        elif işlem=="bölme":
            bölme(num_1,num_2)
        elif işlem=="çikiş":
            print("Programdan çıkılıyor...")
            break
        else:
            print("geçersiz işlem girdiniz tekrar deneyiniz")


main()