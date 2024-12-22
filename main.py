#infa25.2
#1 if kakojta
a = int(input("a = "))
if a <= 0:
    print(f"f(x)= {-1*a}")
elif a > 0 and a < 2:
        print(f"f(x2)= {a**2}")
elif a >= 2:
    print(f"f(x)= {4}")

#2, for 8
a = int(input("a = "))
b = int(input("b = "))
e = 1
for i in range(a, b+1):
    e = i * e
print(e)

#while 3
n = int(input("N = "))
k = int(input("K = "))
if n > k:
    cnt = 0
    while n > k:
        n = n - k
        cnt = cnt + 1
    print("N // K = ", cnt)
    while n > k:
        n = n - k
    print("N % K = ", n)
else:
    if k > n:
        cnt = 0
        while k > n:
            k = k - n
            cnt = cnt + 1
        print("N // K = ", cnt)
        while k > n:
            k = k - n
        print("N % K = ", k)
if n == k:
    print("N % K = 0")
    print("N // K= 1")


#1 infa 25.1
a = (input("chislo = ")); print(f"десятки = ", a[0],";", "единицы = ", a[1])
#or
a = int(input(" a ="))
print("десятки =", a//10, "единицы =", a%10)

#2
a = (input("chislo = ")); print(f"последняя цифра =", a[-1],";", "средняя цифра =", a[-2])

#3
a = int(input("1 =")); b = int(input("2 =")); c = int(input("3 =")); b = [a, b, c]; b.sort(); del b[0]; print(sum(b))

#4
price = int(input("chena = ")); [print(f"{i*10}% = ", price*i/10) for i in range(1, 10+1)]

#5
a = int(input("a ="))
b = int(input("b ="))
c = 1
for i in range (a, b+1):
    c = c*i
print(c)
#or
a = int(input("a =")); b = int(input("b =")); c = 1
for i in range (a, b+1): c = c*i
print(c)
