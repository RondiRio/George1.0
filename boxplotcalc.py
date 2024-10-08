import matplotlib.pyplot as plt
import numpy as np

# Dados
data = [4, 6, 7, 9, 10, 12, 15, 35]

# Criar o boxplot
plt.figure(figsize=(8, 6))
plt.boxplot(data, vert=True, patch_artist=True)

# Adicionar título e rótulos
plt.title('Boxplot da Sequência de Dados', fontsize=14)
plt.ylabel('Valores', fontsize=12)

# Customizar cores do boxplot
box = plt.boxplot(data, patch_artist=True)
colors = ['lightblue']
for median, box_color in zip(box['medians'], colors):
    median.set(color='red', linewidth=2)
for patch in box['boxes']:
    patch.set_facecolor(colors[0])

# Mostrar gráfico
plt.grid(axis='y')
plt.show()
