import pandas as pd
import psycopg2
import yfinance as yf
import mysql.connector

'''SQL de ejemplo: Hacerlo en MySQL primero
NOTA: Asegurarse que la tabla sea la misma que tienen en el dataframe con los nombres de columnas
CREATE TABLE stock_prices (
  O decimal(10,2),
  H decimal(10,2),
  L decimal(10,2),
  C decimal(10,2),
  V bigint,
  D decimal(10,2),
  S decimal(10,2)
);
'''
try:
    conn = mysql.connector.connect(user = 'root', password = 'valeria11',
                                   host = 'localhost',
                                   database = 'etl',
                                   port = '3306'
        
    )
    print("Connected to MySQL successfully!")

    # Continúa con el resto del código...

except mysql.connector.Error as e:  
    print("Unable to connect to MySQL.")
    print(e)

# Verificar que tienen la tabla creada
cur = conn.cursor()
cur.execute("SELECT * FROM stock_prices")
results = cur.fetchall()
print(results)  # Debería ser una lista vacía si la tabla está vacía

# Traer la data
goo = yf.Ticker('GOOG')
hist = goo.history(period="1y")
hist['Date'] = hist.index
hist = hist.reset_index(drop=True)

hist = hist.rename(columns={'Open': 'O', 'High': 'H', 'Low': 'L', 'Close': 'C', 'Volume': 'V', 'Dividends': 'D',
                            'Stock Splits': 'S', 'Date': 'Dat'})
hist = hist.drop(columns=['Dat'])

# Mandar a MySQL
cur = conn.cursor()
table_name = 'stock_prices'
columns = ['O', 'H', 'L', 'C', 'V', 'D', 'S']

# Preparar los datos para la inserción en MySQL
values = [tuple(x) for x in hist.to_numpy()]

# Crear el SQL para la inserción
insert_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"

# Ejecutar la transacción
cur.execute("START TRANSACTION")
cur.executemany(insert_sql, values)
cur.execute("COMMIT")


#