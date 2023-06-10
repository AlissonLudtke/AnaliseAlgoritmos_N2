import matplotlib.pyplot as plt

# Dados para plotagem
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Cria uma nova figura e um conjunto de subplots
plt.figure()

# Plota os dados
plt.plot(x, y)

# Adiciona rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona um título ao gráfico
plt.title('Exemplo de Gráfico')

# Mostra o gráficov
plt.show()
