import pandas as pd
import plotly.graph_objects as go

csv = pd.read_csv('csv/wind_aristeomercado_10m_complete')

i = 0
inicio = 1
fin = 0
while i < len(csv):
    if csv.iloc[i]['val'] < 0 and csv.iloc[i - 1]['val'] > 0:
        fin = i
        df2 = csv.iloc[:inicio-1, :fin-1]
        print("rango de la grafica " + str(inicio) + " - " + str(fin))
        fig = go.Figure(go.Scatter(x=df2['time'], y=df2['val'], name='Velocidad'))

        fig.update_layout(title='Valores de velocidad del veinto en el tiempo',
                          plot_bgcolor='rgb(230, 230,230)',
                          showlegend=True)

        fig.show()
        inicio = fin
    i = i + 1

# fig = go.Figure(go.Scatter(x=csv['time'], y=csv['val'], name='Velocidad'))
#
# fig.update_layout(title='Valores de velocidad del veinto en el tiempo',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#
# fig.show()
