for x in range(1,11):
    if x % 2 == 0:
        print("passei")
        continue
    print(x)
print("etapa 1")

for x in range(1, 11):
    if x == 5:
        print('vou sarir do laço')
        break
        
    print(x)
    
print("fim")