def notas(*n, sit=False):
    """Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r

resp = notas(5.5, 6.9, 3.6, 5.6)
print(resp)
resp = notas(5.5, 6.9, 3.6, 5.6, sit=True)
print(resp)
