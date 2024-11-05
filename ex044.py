preço = float(input('Preço da compra: R$'))
print("""FORMA DE PAGAMENTO:
[ 1 ] A VISTA DINHEIRO/CHEQUE
[ 2 ] A VISTA NO CARTÃO            
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO""")
pagamento = int(input('Qual opção: '))
if pagamento == 1:
    print('Sua compra de R${} custará R${}'.format(preço, preço - 10 / 100 * preço))
elif pagamento == 2:
    print('Sua compra de R${} custará R4{}'.format(preço, preço - 5 / 100 * preço))
elif pagamento == 3:
    print('Você pagará em 2x no cartão, cada parcela sairá por R${} mantendo o preço de R${}'.format(preço / 2, preço))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas?'))
    print('Você pagará em {}x no cartão, cada parcela sairá por R${}, aumentando o valor para R${}'.format(parcelas, (preço + 20 / 100 * preço) / parcelas, preço + 20 / 100 * preço )) 
else:
    print('Zoa baixo mo nengue')
