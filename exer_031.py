dist = float(input('Digite quantos KM fez na viagem -> '))
preço = dist * 0.5 if dist <= 200 else dist * 0.45  # Modo simplificado
print('O valor a pagar por {}km é de {}€'.format(dist, preço))
print('Muito obrigado e conduza com segurança.')
