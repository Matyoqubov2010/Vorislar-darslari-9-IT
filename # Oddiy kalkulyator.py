# Oddiy kalkulyator

# Sonlarni olish
son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

# Amalni tanlash
amal = input("Amalni kiriting (+, -, *, /): ")

# Hisoblash va natijani chiqarish
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
        natija = "Nolga bo‘lish mumkin emas!"
else:
    natija = "Noto‘g‘ri amal kiritildi!"

print("Natija:", natija)
