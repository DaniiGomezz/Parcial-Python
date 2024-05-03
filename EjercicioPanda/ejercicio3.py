import pandas as pd
import matplotlib.pyplot as plt
# Crear un DataFrame a partir de la lista de calificaciones
calificaciones = [
    {"nombre": "Juan", "matematicas": 85, "ciencias": 90, "historia": 75},
    {"nombre": "María", "matematicas": 70, "ciencias": 80, "historia": 85},
    {"nombre": "Pedro", "matematicas": 95, "ciencias": 75, "historia": 90},
    {"nombre": "Ana", "matematicas": 80, "ciencias": 85, "historia": 80},
    {"nombre": "Luis", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Sofía", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Carlos", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Elena", "matematicas": 70, "ciencias": 75, "historia": 85},
    {"nombre": "Javier", "matematicas": 80, "ciencias": 85, "historia": 90},
    {"nombre": "Laura", "matematicas": 75, "ciencias": 70, "historia": 95},
    {"nombre": "Diego", "matematicas": 90, "ciencias": 85, "historia": 75},
    {"nombre": "Paula", "matematicas": 85, "ciencias": 90, "historia": 80},
    {"nombre": "Carmen", "matematicas": 70, "ciencias": 75, "historia": 85}
]

df = pd.DataFrame(calificaciones)


print("punto A")

# A) Calcular el promedio de calificaciones para cada asignatura
promedio_matematicas = df['matematicas'].mean()
promedio_ciencias = df['ciencias'].mean()
promedio_historia = df['historia'].mean()
# muestra por consola el resultado
print("Promedio de matemáticas:", promedio_matematicas)
print("Promedio de ciencias:", promedio_ciencias)
print("Promedio de historia:", promedio_historia)





# B) Encuentra a los estudiantes que tienen las calificaciones más altas en cada asignatura y mostralos junto con sus respectivas calificaciones.
print("punto B")
# Encuentra las calificaciones máximas en cada asignatura
maxima_matematicas = df['matematicas'].max()
maxima_ciencias = df['ciencias'].max()
maxima_historia = df['historia'].max()

# selecciona a todos los estudiantes con la calificación máxima en cada asignatura
top_matematicas = df[df['matematicas'] == maxima_matematicas]
top_ciencias = df[df['ciencias'] == maxima_ciencias]
top_historia = df[df['historia'] == maxima_historia]


#el DataFrame se construye utilizando un diccionario donde las claves representan los nombres de las columnas y los valores son listas que contienen los datos correspondientes.
# crea una lista que contiene el nombre de la asignatura repetido según la cantidad de estudiantes con la calificación más alta en cada asignatura.

df_top = pd.DataFrame({
    'Asignatura': ['Matemáticas'] * len(top_matematicas) +
                  ['Ciencias'] * len(top_ciencias) +
                  ['Historia'] * len(top_historia),
    'Estudiante': list(top_matematicas['nombre']) +
                  list(top_ciencias['nombre']) +
                  list(top_historia['nombre']),
    'Calificación': list(top_matematicas['matematicas']) +
                    list(top_ciencias['ciencias']) +
                    list(top_historia['historia'])
})
#muestra por la consola el resultado final
print(df_top)

print("punto C")
#C) 
aprobados = df.loc[:, ["matematicas", "ciencias", "historia"]] >= 60

# Calcular el porcentaje de aprobados para cada asignatura
porcentaje_aprobados = aprobados.mean() * 100

print("Porcentaje de estudiantes que aprobaron cada asignatura:")
print(porcentaje_aprobados)

# D)Crear un DataFrame que incluya dos columnas una para el nombre del estudiante y la otra para el promedio de las notas de las asignaturas.

print("punto D")
# Calcula el promedio de las calificaciones para cada estudiante
df["promedio"] = df[["matematicas", "ciencias", "historia"]].mean(axis=1)

# crea un DataFrame con el nombre del estudiante y su promedio
df_promedios = df[["nombre", "promedio"]]

# Mostrar el resultado
print("Promedio de calificaciones por estudiante:")
print(df_promedios)


#  Basándote en el DataFrame creado. Utiliza un gráfico de barras donde el eje x represente los nombres de los estudiantes y el eje y represente el promedio de las calificaciones.
plt.figure(figsize=(5, 4))
plt.bar(df["nombre"], df["promedio"], color='skyblue')
plt.xlabel("Estudiantes")
plt.ylabel("Promedio de Calificaciones")
plt.title("Promedio de Calificaciones por Estudiante")
plt.xticks(rotation=50)
plt.show()