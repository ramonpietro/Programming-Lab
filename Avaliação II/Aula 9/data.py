from collections import Counter
import matplotlib.pyplot as plt

def ocorrencias(dado):
    return Counter(dado)

def calcular_frequencia(contador_dado):
    total = sum(contador_dado.values())
    return [count / total for count in contador_dado.values()]

def criar_bins(dado, num_bins):
    min_valor = min(dado)
    max_valor = max(dado)
    bin_width = (max_valor - min_valor) / num_bins
    return [min_valor + i * bin_width for i in range(num_bins + 1)]

def plot_histogram(dado, title='Idades de um grupo', xlabel='Idade', ylabel='Frequencia absoluta', bins=5, rwidth=0.9):
    data_counts = ocorrencias(dado)

    frequecias = calcular_frequencia(data_counts)

    bins = criar_bins(dado, bins)

    plt.title('Idades de um grupo', fontsize=30)
    plt.xlabel('Idade')
    plt.ylabel('Frequencia absoluta')
    plt.hist(idades, 5, rwidth=0.9)
    plt.savefig('grafico.png')
    plt.show


idades=[65,26,67,50,47,73,1,58,2,94,12,22,12,95,25,13,61,41,24,95,
        3,71,53,24,23,44,83,30,19,32,71,66,45,6,99,4,76,27,50,18,58,
        61,53,72,14,78,36,89,6,71,58,69,22,34,38,51,71,83,22,22,36,44,
        16,58,20,49,28,55,21,26,23,41,21,95,18,63,55,2,61,81,39,20,39,
        17,66,60,73,26,54,16,76,83,9,12,15,35,54,11,7,61]

plot_histogram(idades)