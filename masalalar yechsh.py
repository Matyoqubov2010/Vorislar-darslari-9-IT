n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    s += 2 * i - 1
    print(2 * i - 1, end=" ")

print("\nNatija:", s)


a = float(input("a ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

p = 1
for i in range(1, n + 1):
    p *= a
    print(f"{i}-daraja: {p}")

print("\nNatija:", p)


a = float(input("a ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

for i in range(1, n + 1):
    print(f"{a}^{i} = {a ** i}")


a = float(input("a ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    s += ((-1) ** (i - 1)) * (a ** i)

print("Natija:", s)


a = float(input("a ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    s += ((-1) ** (i - 1)) * (a ** i)

print("Natija:", s)



n = int(input("n ni kiriting (n > 0): "))

f = 1
for i in range(1, n + 1):
    f *= i
    print(f"{i}! = {f}")

print("\nNatija:", f)


n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    f = 1
    for j in range(1, i + 1):
        f *= j
    s += f
    print(f"{i}! = {f}")

print("\nNatija:", s)




n = int(input("n ni kiriting (n > 0): "))

s = 1
f = 1
for i in range(1, n + 1):
    f *= i
    s += 1 / f

print("Natija:", s)


x = float(input("x ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 1
f = 1
for i in range(1, n + 1):
    f *= i
    s += (x ** i) / f

print("Natija:", s)



x = float(input("x ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    f = 1
    for j in range(1, 2 * i):
        f *= j
    s += ((-1) ** (i + 1)) * (x ** (2 * i - 1)) / f

print("Natija:", s)


x = float(input("x ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 1
for i in range(1, n + 1):
    f = 1
    for j in range(1, 2 * i + 1):
        f *= j
    s += ((-1) ** i) * (x ** (2 * i)) / f

print("Natija:", s)



x = float(input("x ni kiriting: "))
n = int(input("n ni kiriting (n > 0): "))

s = 0
for i in range(1, n + 1):
    s += ((-1) ** (i - 1)) * (x ** i) / i

print("Natija:", s)
