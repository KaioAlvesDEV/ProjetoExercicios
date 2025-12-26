nums = [int(input('Num1: ')), int(input('Num2: ')), int(input('Num3: '))]
maior = nums[0]
menor = nums[0]

if maior < nums[1]:
    maior = nums[1]
if maior < nums[2]:
    maior = nums[2]

if menor > nums[1]:
    menor = nums[1]
if menor > nums[2]:
    menor = nums[2]

print(f'MAIOR: {maior}\nMENOR: {menor}')

input()
