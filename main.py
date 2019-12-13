import pandas as pd
import plotly.graph_objects as go

csv = pd.read_csv('csv/wind_aristeomercado_10m_complete')

csv = csv[csv.val > 0]
csv = csv[csv.val < 100]

fig = go.Figure(go.Scatter(x=csv['time'], y=csv['val'], name='Velocidad'))

fig.update_layout(title='Valores de velocidad del veinto en el tiempo',
                  plot_bgcolor='rgb(230, 230,230)',
                  showlegend=True)

fig.show()
