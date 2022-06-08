import matplotlib.pyplot as plt

def graficoLineas(lista1, lista2):
    plt.plot( lista1,lista2)
    plt.title('algo en el titulo')
    plt.xlabel('eje x')
    plt.ylabel('ejey')
    plt.savefig('graficoLineas.png')
    
def graficoBarras(lista1, lista2):
    fig, pl = plt.subplots()
    pl.set_ylabel('eje y')
    pl.set_xlabel('eje x')
    pl.set_title('algo en el titulo')
    plt.bar(lista1, lista2)
    plt.savefig('graficoBarras.png')
    
def graficoPuntos(lista1, lista2):
    plt.plot(lista1, lista2, 'o', color="green", label="line 1")
    plt.title('algo en el titulo')
    plt.xlabel('eje x')
    plt.ylabel('ejey')
    plt.legend()
    plt.savefig('graficoPuntos.png')
