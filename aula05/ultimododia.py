max_line = 35

print(f'=' * max_line)
nMin = int(input("Digite o valor minimo: "))
nMax = int(input("Digite o valor maximo: "))
print(f'=' * max_line)


for i in range(nMin, nMax + 1):
    if i % 2 == 0:
        print(f'=' * max_line)
        print(f"{" "*int((max_line/2)-7)}Número {i} é par") # 14
        print(f'=' * max_line)
    else:
        print(f'=' * max_line)
        print(f"{" "*int((max_line/2)-8)}Número {i} é impar") # 16
        print(f'=' * max_line)
        
        
print(f'=' * max_line)
print(f"{" "*int((max_line/2)-2)}FIM")
print(f'=' * max_line)
