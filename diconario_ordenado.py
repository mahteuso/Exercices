from collections import OrderedDict, defaultdict, Counter

dic = OrderedDict(numero1='um', numero3='três', numero4='quatro')
print(dic)

dic['numero5'] = 'cinco'
dic['numero2'] = 'dois'

print(dic)

numeros = [0, 1, 2, 3, 4, 5]

letras = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco']

d = OrderedDict(zip(numeros, letras))
print(d)

di = dict(zip(numeros, letras))

print(di)

du = {letra: numero for letra, numero in zip(letras, numeros)}

print(du)

def none(): return None

print(type(none()))

print('')

print(defaultdict(none))

print('')

pal = """
O endereçamento aberto não introduz nenhuma estrutura de dados nova. Se ocorrer uma colisão, procuramos a disponibilidade no próximo ponto gerado por um algoritmo. O endereçamento aberto é geralmente usado onde o espaço de armazenamento é restrito, ou seja, em processadores embarcados. O endereçamento aberto não é necessariamente mais rápido do que o encadeamento separado.
"""

# pal = list(pal.split())

lista = {}
for palavra in pal.split():
    for letra in palavra:
        lista[letra] = lista.get(letra, 0) + 1

for chave, valor in lista.items():
    print(chave, ':', valor)

print(Counter(pal.split()))

