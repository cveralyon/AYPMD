import sys
import cufflinks as cf
from IPython.display import display, HTML
import plotly as py
import chart_studio
import plotly.graph_objects as go


cf.set_config_file(sharing = 'public' , theme='ggplot',  offline= True)

def grafico_linea(data):
    lineone = [go.Line(y=data.sup_terreno,x=data.index, name='Sup. del terreno')]
    linetwo = [go.Line(y=data.sup_construida,x=data.index, name='Sup. construida')]
    fig = go.Figure(data=lineone)
    fig.add_traces(linetwo)
    # fig.show()
    fig.write_html('./aypmd4/templates/terrenos.html')

def grafico_avaluo(data):
    lineone = [go.Line(y=data.avaluo,x=data.index, name='Avaluo')]
    linetwo = [go.Bar(y=data.sup_terreno,x=data.index, name='Sup. del terreno')]
    fig = go.Figure(data=lineone)
    fig.add_traces(linetwo)
    # fig.show()
    fig.write_html('./aypmd4/templates/avaluo.html')
    
def grafico_tipo_terreno(data):
    langs = []
    dicc = {}
    for i in data.tipo_terreno:
        if i not in dicc:
            dicc[i] = 1
            langs.append(i)
        else:
            dicc[i] += 1
    valores = []
    for f in dicc:
        valores.append(dicc[f])
    trace = go.Pie(labels = langs, values = valores)
    lineone = [trace]
    fig = go.Figure(data=lineone)
    # fig.show()
    fig.write_html('./aypmd4/templates/tipo.html')

    