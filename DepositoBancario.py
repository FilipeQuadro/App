print("Bem-vindo ao sistema de depósito bancário!")
print("Este programa calcula o valor dos juros e o total após um depósito bancário.")

valor =  float(input("Digite o valor do depósito: "))
anos = int(input("Digite o número de anos: "))
taxa = 1.25

juros = (valor*anos*taxa)/100
valor_total = valor + juros
print("O valor dos juros é: R$", juros)
print("O valor total após", anos, "anos é: R$", valor_total)