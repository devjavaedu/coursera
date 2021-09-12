number1 = int(input("Digite um primeiro número inteiro: "))
number2 = int(input("Digite um segundo número inteiro: "))
number3 = int(input("Digite um terceiro número inteiro: "))

if(number1 < number2 and number2 < number3):
    print("crescente")
else:
    print("não está em ordem crescente")