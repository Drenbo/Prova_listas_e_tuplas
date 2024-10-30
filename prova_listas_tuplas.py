grupo_1 = ('vermelho', [5, 8, 9, 6, 9])
grupo_2 = ('azul', [10, 10, 5, 9, 6])
grupo_3 = ('verde', [1, 6, 3, 7, 9])
grupo_4 = ('amarelo', [8, 8, 10, 9, 9])
grupo_5 = ('laranja', [1, 3, 4, 2, 6])

grupos = [grupo_1, grupo_2, grupo_3, grupo_4, grupo_5]
medias = []
classificacao = []

x = 0

# Calcular médias das pontuações
for grupo in grupos:
    soma = sum(grupo[1])
    media = soma / len(grupo[1])
    medias.append(media)
    classificacao.append((grupo[0], media))

# Ordernar médias
medias.sort(reverse = True)
classificacao.sort(key = lambda x : x[1], reverse = True)

# Exibir classificações
while x in range(5):
    print(classificacao[x])
    x += 1