max_line = 100

print(f'=' * max_line)
nMin = int(input(f"{" "*int((max_line/2)-11)}Digite o valor minimo: ")) #22/2 = 11
nMax = int(input(f"{" "*int((max_line/2)-11)}Digite o valor maximo: ")) #22/2 = 11
print(f'=' * max_line)


for i in range(nMin, nMax + 1):
    if i % 2 == 0:
        print(f'=' * max_line)
        print(f"{" "*int((max_line/2)-7)}Número {i} é par") # 14/2 = 7
        print(f'=' * max_line)
    else:
        print(f'=' * max_line)
        print(f"{" "*int((max_line/2)-8)}Número {i} é impar") # 16/2 = 8
        print(f'=' * max_line)
        
        
print(f'=' * max_line)
print(f"{" "*int((max_line/2)-2)}FIM")
print(f'=' * max_line)
