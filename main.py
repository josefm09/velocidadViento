import pandas as pd
import matplotlib.pyplot as plt

colnames = ['time', 'val']
csv = pd.read_csv('csv/dataset_wind_aristeomercado_10m_complete.csv', names=colnames, header=None)

i = 0
inicio = 1
fin = 0
plt.xticks(rotation=90)
while i < len(csv):
    if csv.iloc[i]['val'] < 0 and csv.iloc[i - 1]['val'] > 0:
        fin = i
        df2 = csv.iloc[inicio-1 : fin-1, 0 : 2]
        print("rango de la grafica " + str(inicio) + " - " + str(fin))
        df2.val = pd.to_numeric(df2.val)
        df2.plot(kind='line', x='time', y='val')

        plt.savefig(str(inicio) + " - " + str(fin) + '.png')
        # fig = go.Figure(go.Scatter(x=df2['time'], y=df2['val'], name='Velocidad'))
        #
        # fig.update_layout(title='Valores de velocidad del veinto en el tiempo',
        #                   plot_bgcolor='rgb(230, 230,230)',
        #                   showlegend=True)
        #
        # fig.show()
        inicio = fin
    i = i + 1

# fig = go.Figure(go.Scatter(x=csv['time'], y=csv['val'], name='Velocidad'))
#
# fig.update_layout(title='Valores de velocidad del veinto en el tiempo',
#                   plot_bgcolor='rgb(230, 230,230)',
#                   showlegend=True)
#
# fig.show()
