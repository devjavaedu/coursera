number = int(input("Digite um número inteiro: "))
sum = 0
for digit in str(number):
    sum += int(digit)
print(sum)