import pandas as pd
if FIGURA=="r":
	from figuras import rectangulo
elif FIGURA=="t":
	from figuras import triangulo
elif FIGURA=="c":
	from figuras import circulo

df= pd.read_csv ("figuras.csv")
print ("El archivo ha sido leído")

for index, row in df.ietrrows ():
	print (f"Fila {index}: FIGURA={row['FIGURA']}, 	MEDIDA1={row['MEDIDA1']}, MEDIDA2= {row['MEDIDA2']}")






















































