sumpar = 0
sumimp = 0

for i in range(101):
    if (i % 2 == 0):
        sumpar+=i
    else:
        sumimp+=i    
        
print(sumpar, sumimp, sumpar+sumimp)