import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.path.dirname(os.path.abspath(__file__))

colnames = ['time', 'val']
csv = pd.read_csv('csv/dataset_wind_aristeomercado_10m_complete.csv', names=colnames, header=None)

i = 0
inicio = 1
fin = 0
rango = ""
while i < len(csv):
    fin = i + 24
    valor = csv.iloc[fin, 1]
    df2 = csv.iloc[inicio: fin, 0: 2]
    print("rango de la grafica " + str(inicio) + " - " + str(fin))
    df2.val = pd.to_numeric(df2.val)
    df2.plot(kind='line', x='time', y='val', legend=False)

    plt.axis('off')
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0,
                        hspace=0, wspace=0)
    plt.margins(0, 0)

    if 0 <= valor <= 0.05:
        rango = "0 - 0.05"
    elif 0.05 < valor <= 0.1:
        rango = "0.05 - 0.1"
    elif 0.1 < valor <= 0.15:
        rango = "0.1 - 0.15"
    elif 0.15 < valor <= 0.2:
        rango = "0.15 - 0.2"
    elif 0.2 < valor <= 0.25:
        rango = "0.2 - 0.25"
    elif 0.25 < valor <= 0.3:
        rango = "0.25 - 0.3"
    elif 0.3 < valor <= 0.35:
        rango = "0.3 - 0.35"
    elif 0.35 < valor <= 0.4:
        rango = "0.35 - 0.4"
    elif 0.4 < valor <= 0.45:
        rango = "0.4 - 0.45"
    elif 0.45 < valor <= 0.5:
        rango = "0.45 - 0.5"
    elif 0.5 < valor <= 0.55:
        rango = "0.5 - 0.55"
    elif 0.55 < valor <= 0.6:
        rango = "0.55 - 0.6"
    elif 0.6 < valor <= 0.65:
        rango = "0.6 - 0.65"
    elif 0.65 < valor <= 0.7:
        rango = "0.65 - 0.7"
    elif 0.7 < valor <= 0.75:
        rango = "0.7 - 0.75"
    elif 0.75 < valor <= 0.8:
        rango = "0.75 - 0.8"
    elif 0.8 < valor <= 0.85:
        rango = "0.8 - 0.85"
    elif 0.85 < valor <= 0.9:
        rango = "0.85 - 0.9"
    elif 0.9 < valor <= 0.95:
        rango = "0.9 - 0.95"
    elif 0.95 < valor <= 1:
        rango = "0.95 - 1"

    plt.savefig(path + '/' + rango + '/' + str(i) + ' - ' + str(csv.iloc[fin, 1]) + '.png', bbox_inches='tight', pad_inches=0, dpi=25)
    inicio = inicio + 1
    i = i + 1
