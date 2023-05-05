comidas = dict(arroz='feijão', macarrão='molho', feijoada='porco')

for comida, tempero in comidas.items():
    print(comida, ': ', tempero)


comidas.update({'molho': 'tempero'})

print(comidas)

comidas['molho'] = 'tomate'

print(comidas)
print('')

print('Compreensão de dicionários')

digito = [0, 1, 2, 3, 4]

string = ['zero', 'um', 'dois', 'três', 'quatro']

num_letras = {digito: string for digito, string in zip(digito, string)}

print(num_letras)

novo_dic = dict(zip(digito, string))

print(novo_dic)

#help(dict)

a = dict(valor1='um', valor2='dois', valor3='três', valor4='quatro')
print(a)
print('')


for k, v in a.items():
    print(f'{a[k]} = {v}')