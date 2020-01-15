import pandas as pd
import matplotlib.pyplot as plt

colnames = ['time', 'val']
csv = pd.read_csv('csv/wind_aristeomercado_10m_complete', names=colnames, header=None)

csv = csv[csv.val > 0]

i = 0
inicio = 1
fin = 0
plt.gca().set_axis_off()
plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                    hspace=0, wspace=0)
plt.margins(0, 0)
while i < len(csv):
    fin = i + 24
    df2 = csv.iloc[inicio: fin, 0: 2]
    print("rango de la grafica " + str(inicio) + " - " + str(fin))
    df2.val = pd.to_numeric(df2.val)
    df2.plot(kind='line', x='time', y='val')

    plt.savefig(str(i) + ' - ' + str(csv.iloc[fin, 1]) + '.png', bbox_inches='tight', pad_inches=0, dpi=25)
    inicio = inicio + 1
    i = i + 1
