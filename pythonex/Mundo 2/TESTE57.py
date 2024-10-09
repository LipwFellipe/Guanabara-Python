res = "d"
while res not in "MmFf":
    res = str(input("Qual é o seu genêro? "))
match res:
    case "F": print("Seu genero é Feminino.")
    case "M": print("Seu genro é Masculino")
    case "f": print("Seu genero é Feminino.")
    case "m": print("Seu genro é Masculino")
