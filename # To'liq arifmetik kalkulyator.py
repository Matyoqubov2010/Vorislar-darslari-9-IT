# To'liq arifmetik kalkulyator

def kalkulyator():
    while True:
        try:
            son1 = float(input("Birinchi sonni kiriting: "))
            son2 = float(input("Ikkinchi sonni kiriting: "))
            amal = input("Amalni kiriting (+, -, *, /, **, %): ")

            if amal == '+':
                natija = son1 + son2
            elif amal == '-':
                natija = son1 - son2
            elif amal == '*':
                natija = son1 * son2
            elif amal == '/':
                if son2 != 0:
                    natija = son1 / son2
                else:
                    print("Xato: Nolga bo‘lish mumkin emas!")
                    continue
            elif amal == '**':
                natija = son1 ** son2
            elif amal == '%':
                if son2 != 0:
                    natija = son1 % son2
                else:
                    print("Xato: Nolga bo‘lish mumkin emas!")
                    continue
            else:
                print("Noto‘g‘ri amal kiritildi!")
                continue

            print(f"Natija: {natija}")
        except ValueError:
            print("Iltimos, son kiriting!")

        yana
