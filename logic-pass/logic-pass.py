# This Is The Answer To The Second Question :
x= 3
y = 99
print("Prime Numbers Between", x, "and", y, "are:")

for num in range(x, y + 1):
        for z in range(2, num):
            if (num % z) == 0:
                break
        else:
            print(num)