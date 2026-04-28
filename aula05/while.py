i = 0
num = int(input("Digite um número para a tabuada: "))
max_line = 20

print("=" * max_line)
while i <= 10:
    print(f"{num} X {i} = {num*i}")
    i+=1
print("=" * max_line)
