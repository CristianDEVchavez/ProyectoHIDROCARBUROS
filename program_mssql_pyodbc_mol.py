# Mssql -> Pandas -> Exporta a csv
# Importar las Librerias:
import pandas as pd
import pyodbc

# Configuración de la conexión a SQL Server
server = '10.210.23.10'
database = 'MOL'
username = 'Sa'
password = '"#$%//0956EDFtskJSSDSD"'

# Establecer la conexión
conexion = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Leer datos de SQL Server
query = "SELECT * FROM ESTACIONES"

# Creamos DataFrame 
df = pd.read_sql(query, conexion)

# Definir rutas de archivos de salida
csv_file= r'moleds.csv'


df.to_csv(csv_file, index=False)
print(f'Se han guardado los datos en "{csv_file}" satisfactoriamente.')

# Cerrar la conexión
conexion.close()
print("Conexión cerrada.")
