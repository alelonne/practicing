cod_vend = int(input("Digite o código do vendedor: "))
qtd_vendas = int(input("Digite a quantidade de vendas desse vendendor: "))

comissao = qtd_vendas * 0.015

print(f"O vendedor, de código: {cod_vend}, obteve a venda total de {qtd_vendas} produtos, totalizando a comissão de {comissao}")