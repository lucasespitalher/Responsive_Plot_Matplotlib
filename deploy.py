# o código foi feito em função das constantes RU e LISTA_X
# portanto, os valores do RU podem ser alterados e LISTA_X pode receber novos valores, ter valores removidos e(ou) valores alterados
# a único requisito é que os valores sejam números e preferencialmente com no máximo duas casas decimais
# o gráfico e os cálculos plotados são ajustados de acordo com os valores de RU e LISTA_X

import matplotlib.pyplot as plt    # importando pyplot de matplotlib


RU = (1, 5, 2)                     # tupla com três últimos números do RU
LISTA_X = [5,7,9,15,19,5,7,1,-1,6] # lista com valores de X


def aplicar_equacao(X, RU): # método para realizar o cálculo da equação
    a, b, c = RU            # unpacking da tupla para utilizar os números do RU no cálculo
    y = a*X + X*b - c       # Cálculando y
    return y                # Retorna o resultado de y


# lista_resultados --> utilizada para plotar a reta e os pontos no gráfico
lista_resultados = [] # lista que recebe os resultados dos cálculos
for x in LISTA_X:     # loop para percorrer a constante LISTA_X
    lista_resultados.append(aplicar_equacao(x, RU)) # realiza o cálculo com cada valor de x da LISTA_X e adiciona os resultados em lista_resultados

# eixo_x --> utilizado para plotar a reta e os pontos no gráfico
eixo_x = [] # lista que armazena uma sequência de 1 a x sendo x a quantidade de resultados em lista_resultados (1,2,3...N)
for num in range(len(lista_resultados)):    # loop range no tamanho de lista_resultado
    eixo_x.append(num + 1)                  # eixo_x recebe o valor de num + 1. Quando num == 0 --> eixo_x recebe 1...


fig, ax = plt.subplots(1, 2, layout='constrained') # cria uma figura com 1 linha e 2 colunas para plot do gráfico e dos cálculos
ax[0].set_title("Gráfico dos Resultados")   # define o título do gráfico
ax[0].plot(eixo_x, lista_resultados)        # plota/imprime um linha utilizando os valores de lista_resultado como pontos
ax[0].plot(eixo_x, lista_resultados, 'bo')  # plota/impirme pontos na tela nas coordenadas do eixo_x com os valores de lista_resultado
for i in range(len(lista_resultados)):      # loop range no tamanho de lista_resultado
    ax[0].annotate(lista_resultados[i], (eixo_x[i]-0.25, lista_resultados[i]+2)) # plota/imprime os valores de lista_resultado no gráfico

ax[0].set_xlabel('Eixo X')  # define a legenda do eixo X
eixo_x_axis = [0]           # lista que recebe os valores de eixo_x e margens para exebição do gráfico
    # eixo_x_axis é a lista utilizada para definir o eixo_x do gráfico. Além dos valores de eixo_x é iniciada com zero e contém um número a mais.
    # isto permite que existam margens laterais na exibição do gráfico evitando que a linha e os pontos se choquem com as paredes do quadro
    # eixo_x == [1,2,3] --- eixo_x_axis == [0,1,2,3,4]

for num in eixo_x:                      # loop que percorre os valores de eixo de x
    eixo_x_axis.append(num)             # eixo_x_axis recebe os valores de eixo_x
eixo_x_axis.append(eixo_x_axis[-1] + 1) # adiciona um último valor em eixo_x_axis
ax[0].set_xticks(eixo_x_axis)           # define eixo_x_axis como os valores do eixo X do gráfico

ax[0].set_ylabel('Eixo Y')              # define a legenda do eixo Y
eixo_y_axis = [min(lista_resultados) - 10] # lista que recebe os valores com margens para definir o eixo Y da figura
    ### VERIFICAR SE HÁ NÚMERO NEGATIVO EM LISTA_X
tamanho_y = 10 + ((max(lista_resultados) // len(lista_resultados)) * len(eixo_x)) # variável que define o tamanho do eixo Y
    # 10 é utilizado como margem de segurança para exibição. O restante do cálculo serve para identificar o ponto alto mínimo necessário
    # para que todos os valores plotados aparecam corretamente no gráfico.
while eixo_y_axis[-1] <= tamanho_y: # enquanto o último valor da lista for menor ou igual a(o) tamanho/altura mímina necessária faça:
    eixo_y_axis.append(eixo_y_axis[-1] + (max(lista_resultados)//len(lista_resultados))) # cria a escala do eixo Y
    # cada valor adicionado em eixo_y_axis é a soma do último valor inserido com a distãncia entre os pontos da escala
    # a distância está sendo cálculada pegando o maior número da lista_resultado e dividendo ele pela quantidade de resultados
ax[0].set_yticks(eixo_y_axis) # define eixo_y_axis como os valores do eixo Y do gráfico 

lista_y = [0]                               # lista que recebe os valores do eixo Y para a segunda figura
for num in range(len(lista_resultados)):    # loop range no tamanho de lista_resultado
    lista_y.append(lista_y[-1] + 25)        # lista_y recebe o valor da última posição mais 25 em cada loop
    # 25 é um valor número encontrado em testes adequado e suficiente para exibir as 4 linhas de cada cálculo

axis_y = [num for num in reversed(lista_y)] # armazenando em axis_y a lista_y invertida utilizando list comprehension e reversed

ax[1].set_title(f"Equação: y = {RU[0]}x + x{RU[1]} – {RU[2]}")  # define a equação como título da segunda figura
for i in range(len(lista_resultados)):                          # loop range no tamanho de lista_resultado
    ax[1].annotate(f"x = {LISTA_X[i]}", (0.1, axis_y[i]-5))     
        # adiciona uma linha de texto nas coordenandas x=0.1 y=valor[i] de axis_y - 5
        # -5 é utilizado para o texto não sobreescrever o título da figura
    ax[1].annotate(f"y = {RU[0]}*{LISTA_X[i]} + {LISTA_X[i]}*{RU[1]} - {RU[2]}", (0.2, axis_y[i]-10))
        # adiciona uma linha de texto nas coordenandas x=0.2 y=valor[i] de axis_y - 10
        # -10 é utilizado para o texto fique abaixo do texto inserido anteriomente
    ax[1].annotate(f"y = {RU[0]*LISTA_X[i]} + {LISTA_X[i]*RU[1]} - {RU[2]}", (0.2, axis_y[i]-15))
        # adiciona uma linha de texto nas coordenandas x=0.2 y=valor[i] de axis_y - 15
        # -15 é utilizado para o texto fique abaixo do texto inserido anteriomente
    ax[1].annotate(f"y = {RU[0]*LISTA_X[i] + LISTA_X[i]*RU[1] - RU[2]}", (0.2, axis_y[i]-20))
        # adiciona uma linha de texto nas coordenandas x=0.2 y=valor[i] de axis_y - 20
        # -20 é utilizado para o texto fique abaixo do texto inserido anteriomente

    # supondo que a lista axis_y tenha a seguinte estrutura: [75,50,25,0]
    # no primeiro loop i é igual a 0, ou seja, o valor de axis_y[i] é igual a 75
    # então o primeiro annotate será adicionado em x=0.1 e y=70 (75 - 5)
    # já o segundo annotate será adicionado em x=0.2 e y=65 (75 - 10), logo abaixo do annotate anterior 
    # o terceiro annotate será adicionado em x=0.2 e y=60 (75 - 15) e assim sucessivamente para os demais annotate
    # no segundo loop i será igual a 1, ou seja, o valor de axis_y[i] agora é 50
    # portanto, o primeiro annotate será adicionado em x=0.1 e y=45 (50 - 5)...
    # assim segue o loop laço até exibir todos os cálculos na tela

ax[1].set_xticks([0,1])                     # define os valore do eixo X da segunda figura
ax[1].set_yticks([0,axis_y[0]])             # define os valore do eixo Y da segunda figura
ax[1].xaxis.set_visible(False)              # torna invisível o eixo X
ax[1].yaxis.set_visible(False)              # torna invisível o eixo Y
ax[1].spines['top'].set_visible(False)      # torna invisível a borda superior do quadrante
ax[1].spines['left'].set_visible(False)     # torna invisível a borda esquerda do quadrante
ax[1].spines['right'].set_visible(False)    # torna invisível a borda direita do quadrante
ax[1].spines['bottom'].set_visible(False)   # torna invisível a borda inferior do quadrante

plt.show()  # exibe a figura