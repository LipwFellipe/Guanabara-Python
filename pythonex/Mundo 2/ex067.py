while True:
    tabu = int(input("Quer ver a Tabuada de qual valor?"))
    if tabu < 0:
        break
    print(f"{'Tabuada':=^40}")
    print(f"""{tabu} * 1 = {tabu*1}
{tabu} * 2 = {tabu*2}
{tabu} * 3 = {tabu*3}
{tabu} * 4 = {tabu*4}
{tabu} * 5 = {tabu*5}
{tabu} * 6 = {tabu*6}
{tabu} * 7 = {tabu*7}
{tabu} * 8 = {tabu*8}
{tabu} * 9 = {tabu*9}
{tabu} * 10 = {tabu*10}
""")
print("Programa terminado!!!")