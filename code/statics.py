
# coding: utf-8

# In[3]:

from matplotlib import pyplot as plt

def grafic_line(plt):
    years = [1950,1960,1970,1980,1990,2000,2010]
    gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

    plt.plot(years,gdp,color='green',marker='o',linestyle='solid')

    plt.title('GDP Nominal')

    plt.ylabel("Bilhões de Dólares")

    plt.show()

def grafic_bar(plt):
    movies = ["Annie Hall","Ben Hur","Casablanca","Gandhi","Weest Side story"]
    num_oscars = [5,11,3,8,10]

    #por padrão as barras tem tamanho 0.8 , então será adicionado 0.1 ás coordenadas a esquerda para que a barra seja centralizada
    xs =[i + 0.1 for i,_ in enumerate(movies)]

    plt.bar(xs,num_oscars)

    plt.ylabel("# de Premiações")
    plt.title("Meus Filmes Favoritos")

    #nomeia o eixo x com nomes de filmes na barra central
    plt.xticks([i+0.5 for i,_ in enumerate(movies)],movies)
    plt.show()

def grafic_line_multiple(plt):
    variance = [1,2,4,8,16,32,64,128,256]
    bias_squared = [256,128,64,32,16,8,4,2,1]
    total_error = [x+y for x,y in zip(variance,bias_squared)]
    xs = [i for i,_ in enumerate(variance)]

    #faz varias chamadas para plt.plot para mostrar multiplas séries no mesmo grafico
    plt.plot(xs,variance,'g-',label='variance') #linha verde sólida
    plt.plot(xs,bias_squared,'r-.',label='bias^2') #linha com ponto tracejado
    plt.plot(xs,total_error,'b:',label='total error') #linha com pontlhado azul

    plt.legend(loc=9)#loc=9 significa top center
    plt.xlabel("complexidade do modelo")
    plt.title("Compromisso entre Polarização e Variância")
    plt.show()

if __name__ == "__main__":
    #grafic_bar(plt)
    grafic_line_multiple(plt)


# In[20]:


from collections import Counter
from matplotlib import pyplot as plt
import math

num_friends = [100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def grafic_cont(plt):
    friends_counts = Counter(num_friends)
    xs = range(101) #o valor maior é 100
    ys = [friends_counts[x] for x in xs]
    plt.bar(xs,ys)
    plt.axis([0,101,0,25])
    plt.title("Hitograma da Contagem de amigos")
    plt.xlabel("# de Amigos")
    plt.ylabel("# de pesssoas")
    plt.show()


num_points = len(num_friends)
largest_value = max(num_friends) #maior valor
smallest_value = min(num_friends) #menor valor
sorted_value = sorted(num_friends)
smallest_value = sorted_value[0]
second_smallest_value = sorted_value[1]
second_largest_value = sorted_value[-2]

def mean(x): #Média
    return sum(x)/len(x)

def median(x): #Mediana
    #encontra o valor mais ao meio de x
    n = len(x)
    sorted_x = sorted(x)
    midpoint = n // 2

    if n % 2 == 1:
        #se for ímpar, retorna o valor do meio
        return sorted_x[midpoint]
    else:
        # se for par, retorna a média dos valores do meio
        lo = midpoint - 1
        hi = midpoint
        return (sorted_x[lo]+sorted_x[hi]) / 2

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def mode(x):
    #retorna uma lista, pode haver mais de uma moda
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items()
               if count == max_count]

# Produto escalar
def dot(v,w):
    return sum(v_i * w_i
              for v_i,w_i in zip(v,w))
#soma dos quadrados de um vetor
def sum_of_squares(v):
    return dot(v,v)

def data_range(x): #amplitude
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x): #variança , medida de dispersão
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations)/(n-1)

############
#correlação

daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]
def covariance(x,y):
    n = len(x)
    return dot(de_mean(x),de_mean(y)) / (n - 1)


if __name__ == "__main__":
    grafic_cont(plt)
    print("Minima: ",largest_value)
    print("Máxima: ",smallest_value)
    print("média: ",'%.2f'%mean(num_friends))
    print("mediana: ",median(num_friends))
    print("moda: ",mode(num_friends))
    print("variancia: ",variance(num_friends))
    print("covariancia: ",covariance(num_friends,daily_minutes))
