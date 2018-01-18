
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

