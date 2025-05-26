"""import pandas as pd
df=pd.read_csv('C:\\VS Code\\s3_ventas.csv',names=('ID_Venta', 'ID_Cliente', 'ID_Producto', 'Fecha', 'Cantidad', 'Precio_Unitario'),header=0,dtype={'ID_Venta':int, 'ID_Cliente':int, 'ID_Producto':int, 'Fecha':str, 'Cantidad':int, 'Precio_Unitario':float})
df['Fecha']=pd.to_datetime(df['Fecha'])
df['ingreso_total']=df['Precio_Unitario']*df['Cantidad']
ingreso_medio=float(f'{(df['ingreso_total'].mean()):.3f}')
print(ingreso_medio)
ingreso_por_cliente=df.groupby('ID_Cliente').agg({'ingreso_total':'sum'}).sort_values(by=['ingreso_total'],ascending=False)
print(ingreso_por_cliente)
filter=ingreso_por_cliente['ingreso_total']>ingreso_medio
print(df[filter])
"""
#---3,2---- 3.2: Calcular el ingreso total por cliente, ordenarlo de manera descendente, y mostrar solo los clientes cuyo ingreso total sea mayor al ingreso promedio de todos los clientes.
import pandas as pd
df = pd.read_csv('C:\\VS Code\\s3_ventas.csv', names=('ID_Venta', 'ID_Cliente', 'ID_Producto', 'Fecha', 'Cantidad', 'Precio_Unitario'), header=0, dtype={'ID_Venta': int, 'ID_Cliente': int, 'ID_Producto': int, 'Fecha': str, 'Cantidad': int, 'Precio_Unitario': float})
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['ingreso_total'] = df['Precio_Unitario'] * df['Cantidad']

ingreso_medio = float(f'{(df['ingreso_total'].mean()):.3f}')
ingreso_por_cliente = df.groupby('ID_Cliente').agg({'ingreso_total': 'sum'}).sort_values(by=['ingreso_total'], ascending=False).reset_index()
df = df.merge(ingreso_por_cliente, on='ID_Cliente', suffixes=('', '_xcliente'))
filter = df['ingreso_total_xcliente'] > ingreso_medio
#print(df[filter])


#3.3: Generar un gráfico de barras que muestre el ingreso total por mes (agrupando por mes y año), asegurándose de que los meses estén ordenados cronológicamente.

"""def ingreso_por_mes():
    for i in    #.agg({'ingreso_total': 'sum'})
"""
#3.3: Generar un gráfico de barras que muestre el ingreso total por mes (agrupando por mes y año), asegurándose de que los meses estén ordenados cronológicamente.
from datetime import datetime
from matplotlib import pyplot as plt
val_per_month= df.groupby(df['Fecha'].dt.month).agg({'ingreso_total': 'sum'})
chart=  val_per_month.plot(kind='bar')

# Labels and title
plt.xlabel('Month')
plt.ylabel('Total Ingreso')
plt.title('Total Ingreso per Month')

# Show the plot
plt.show()

