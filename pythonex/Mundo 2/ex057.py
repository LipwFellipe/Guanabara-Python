print("------Dados Pessoais------")
nome = str(input("Qual o nome dele? "))
idd = int(input("Quantos anos ele tem? "))
secso = str(input("Qual o secso? ")).upper().strip()
while secso not in ["M", "F"]:
    print("Responda apenas com M ou F")
    secso = str(input("Qual o secso?")).upper().strip()
if secso == "M":
    secso = "Masculino"
if secso == "F":
    secso = "Feminino"
print(f"Seu nome é {nome}, tem {idd} anos e é do sexo {secso}")
