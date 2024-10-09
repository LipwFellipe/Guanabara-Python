i = int(input("Qual o primeiro valor da fatorial? "))
res = 1
while i > 0:
    print(i, end="")
    res *= i
    i -= 1
    if i <= 0:
        print(" = ", end="")
    else:
        print(" x ", end="")
print(res)
