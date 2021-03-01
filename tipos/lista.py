nums = [1, 2, 3]
print(type(nums))

nums.append(3) # acrecenta no ultimo indice
nums.append(4)
nums.append(5)

print(nums)
print(len(nums))

nums[3] = 100 # altera o valor do indice 3 para 100
nums.insert(0, -200) # acrescenta no indice 0
print(nums) # retorna a lista inteira
print(nums[-1]) # retorna o ultimo elemento da lista 
print(nums[-2]) # retorna o penultimo elemento da lista 
print(len(nums))