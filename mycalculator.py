def calculator():
    print("Sadə Kalkulyator")
    print("1. Toplama")
    print("2. Çıxma")
    print("3. Vurma")
    print("4. Bölmə")


    seçim = input("Əməliyyatı seçin (1-4): ")

    if seçim in ['1', '2', '3', '4']:
        a = float(input("Birinci rəqəmi daxil edin: "))
        b = float(input("İkinci rəqəmi daxil edin: "))


        if seçim == '1':
            print(f"Nəticə: {a + b}")
        elif seçim == '2':
            print(f"Nəticə: {a - b}")
        elif seçim == '3':
            print(f"Nəticə: {a * b}")
        elif seçim == '4':
            if b != 0:
                print(f"Nəticə: {a / b}")
            else:
                print("Sıfıra bölmək mümkün deyil!")
    else:
        print("Yanlış seçim etdiniz!")

calculator()