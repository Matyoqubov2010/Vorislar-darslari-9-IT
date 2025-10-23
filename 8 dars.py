
# ismlar = ["Abror", "Mahmud", "Zuhra"]

# for ism in ismlar:
#     print(f"Salom {ism}, bugun choyxonaga boramizmi?")


# sonlar = [5, -3, 10, 2.5, -7.8]
# print(sonlar[0] + sonlar[2])  # 5 + 10 = 15
# print(sonlar[3] * 2)          # 2.5 * 2 = 5
# sonlar[1] = sonlar[1] + 10    # -3 ni 7 ga o‘zgartirdik


# t_shaxslar = ["Imom Buxoriy", "Amir Temur", "Alisher Navoiy"]
# z_shaxslar = ["Bill Gates", "Elon Musk", "Cristiano Ronaldo"]
# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(1)

# print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa {z_shaxs} bilan suhbat qilishni istar edim.")


friends = []
friends.append("Abror")
friends.append("Mahmud")
friends.append("Zuhra")
friends.append("Madina")
friends.append("Sardor")
friends.remove("Zuhra")  # Zuhra kela olmaydi
friends.insert(0, "Javohir")      # boshiga
friends.insert(2, "Dilshod")      # o‘rtasiga
friends.append("Aziza")           # oxiriga
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(1))

print("Mehmonlar ro‘yxati:", mehmonlar)
