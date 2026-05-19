
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datos/partidos_voley.csv")

ganadores = []

for i in range(len(df)):

    if df["sets_local"][i] > df["sets_visitante"][i]:
        ganadores.append(df["equipo_local"][i])

    else:
        ganadores.append(df["equipo_visitante"][i])

df["ganador"] = ganadores

victorias = df["ganador"].value_counts()

for equipo, cantidad in victorias.items():
    print(equipo, ":", cantidad, "victorias")

victorias.plot(kind="bar")

plt.title("Victorias por equipo")
plt.xlabel("Equipos")
plt.ylabel("Cantidad de victorias")

plt.savefig("resultados/grafico_victorias.png")

plt.show()
