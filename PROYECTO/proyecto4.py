#CIENCIA DE DATOS
#Realizar un programa que realice un Gráfico de Matplotlib
#Realizar un reporte con el gráfico

#CASOS FISCALES
#Número de casos fiscales ingresados y atendidos 2021

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_data = pd.read_csv('2021_CasosFiscales.csv', sep=";" ,usecols=["tipo_caso","ingresado","atendido"])

"""
print(df_data.head())"""

x=df_data["ingresado"]
x2=df_data["atendido"]
y=df_data["tipo_caso"]
"""an= 0.3"""

"""df_data.plot(x=["ingresado","atendido"],y="tipo_caso",kind="bar", figsize=(20,10),color=("g","c"), widht= 0.8)"""

fig, ax = plt.subplots(figsize=(12,6), dpi=100)



ax.barh(y ,x, height=0.5, color="g", edgecolor="black", label="Ingresados",)
ax.barh(y , x2 , height=0.5, color= "c", edgecolor="black", label= "Atendidos")



plt.yticks(rotation=45)
"""plt.xlim(min("ingresado"))""" 

plt.title("Número de casos fiscales Ingresados y Antendidos 2021 ")
plt.xlabel("Casos Ingresados y Atendidos")
plt.ylabel("Tipos_Casos")
plt.legend()
plt.show()
