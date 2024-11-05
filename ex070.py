total = produtos_mais_1000 = produtos_comprados = preço_produto_mais_barato = 0
print('-'*50)
print('        LOJA')
print('-'*50)
while True:
    nome_produto = str(input('Nome do produto: ')).strip()
    preço_produto = float(input('Preço do produto: R$').strip())
    produtos_comprados += 1

    total += preço_produto
    if preço_produto > 1000:
        produtos_mais_1000 += 1
    if produtos_comprados == 1:
        nome_produto_mais_barato = nome_produto
        preço_produto_mais_barato = preço_produto
    else:
        if preço_produto_mais_barato > preço_produto:
            preço_produto_mais_barato = preço_produto
            nome_produto_mais_barato = nome_produto

    while True:
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Opção Inválida! Tente de novo.')
        else:
            break
    if continuar == 'N':
        print(f'Finalizando as compras...')
        break
print('-'*50)
print(f'Total: R${total}')
print(f'Produtos mais de R$1000: {produtos_mais_1000}')
print(f'Produto mais barato: {nome_produto_mais_barato} custando R${preço_produto_mais_barato}')
print('-'*50)