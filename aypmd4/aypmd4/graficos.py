import matplotlib.pyplot as plt

def graficoLineasTipoSuelo(lista1, lista2):
    fig, ax = plt.subplots()
    ax.set_ylabel('Sup. Construida')
    ax.set_xlabel('Tipo')
    ax.set_title('Sup. Construida V/S Tipo')
    plt.bar(lista1, lista2)
    plt.savefig('graficoBarras.jpg')
    plt.close()
    
def graficoPuntosAvaluoFiscal(lista1, lista2):
    plt.plot(lista1, lista2, 'o', color="green")
    plt.title('Sup. Construida V/S Avaluo Fiscal')
    plt.xlabel('Avaluo Fiscal')
    plt.ylabel('Sup. Construida')
    plt.legend()
    plt.savefig('graficoPuntosAvaluoFiscal.jpg')
    plt.close()
    
def graficoPuntosSupTerreno(lista1, lista2):
    plt.plot(lista1, lista2, 'o', color="orange")
    plt.title('Sup. Construida V/S Sup. Terreno')
    plt.xlabel('Sup. Terreno')
    plt.ylabel('Sup. Construida')
    plt.legend()
    plt.savefig('graficoPuntosSupTerreno.jpg')
    plt.close()

    