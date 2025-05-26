



















#3.1 Importación CSV
import pandas as pd

df=pd.read_csv('s3_ventas.csv',header=0,delimiter=',')
#print(df)
ingreso_total= df['Precio_Unitario'].groupby(df['ID_Cliente'])
print(ingreso_total)
#print(ingreso_total)
