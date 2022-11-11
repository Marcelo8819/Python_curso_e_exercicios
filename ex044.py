'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

print('{:=^40}'.format('Lojas Celo') )
preco = float(input('Preço das compras: R$'))
print(''' FORMAS DE PAGAMENTO
[1] à vista, dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2 
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    total_parcelas = int(input('Número de parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(total_parcelas,parcela))
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,total))
   


