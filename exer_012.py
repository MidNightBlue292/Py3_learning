# desconto de 5%
produto = float(input('Qual o preço do produto? € '))
desconto = produto - (produto * 5 / 100)
print('O produto que custava {:.2f}€ agora custa {:.2f}€ com 5% de desconto.'.format(produto, desconto))
