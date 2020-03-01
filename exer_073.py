clubes = ('Benfica','FC Porto','Famalicao','Sporting','Vitória SC','Rio Ave','Braga','Tondela','Boavista',
          'Gil Vicente','Vitória FC','Belenenses','Moreirense','Santa Clara','Maritimo','Portimonense',
          'Ferreira','Aves')
print(f'Existem {len(clubes)} clubes na primeira liga.')
print(clubes)
print('Os cinco primeiros classificados são:')
print(clubes[:5])
print('Os quatro últimos classificados são:')
print(clubes[-4:])
print('Clubes por ordem alfabética:')
print(sorted(clubes))
print(f'O FC Porto está na {clubes.index("FC Porto")+1}ª posição')
