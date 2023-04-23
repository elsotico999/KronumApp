import os
import tkinter as tk
from PIL import Image, ImageTk
from datos_funciones.funciones import find_stats, find_features, gb, model_db
from datos_funciones.funciones import banderas, size, rank, df_wc_ranked, results, df, team_stats_raw, stats_df, full_df, base_df, base_df_no_fg


# Función para mostrar las banderas de ambos equipos
def mostrar_bandera():
    pais_1 = team_1_entry.get().lower()
    pais_2 = team_2_entry.get().lower()
    archivo_imagen_1 = pais_1 + ".png"
    archivo_imagen_2 = pais_2 + ".png"
    imagen_1 = Image.open("banderas_min/" + archivo_imagen_1)
    imagen_2 = Image.open("banderas_min/" + archivo_imagen_2)
    imagen_1 = imagen_1.resize((150, 100)) # Ajustar el tamaño de la imagen
    imagen_2 = imagen_2.resize((150, 100)) # Ajustar el tamaño de la imagen
    imagen_1 = ImageTk.PhotoImage(imagen_1)
    imagen_2 = ImageTk.PhotoImage(imagen_2)
    bandera_label_1.config(image=imagen_1)
    bandera_label_2.config(image=imagen_2)
    bandera_label_1.image = imagen_1 # Actualizar la imagen mostrada
    bandera_label_2.image = imagen_2 # Actualizar la imagen mostrada


# Crear la ventana principal
window = tk.Toplevel()
window.title("KronumApp")

# Configurar la ventana principal
window.geometry("500x300")  # Definir tamaño y posición de la ventana






# Crear las entradas de texto
team_1_entry = tk.Entry(window)
team_1_entry.grid(row=0, column=5, padx=10, pady=10)
team_2_entry = tk.Entry(window)
team_2_entry.grid(row=0, column=6, padx=10, pady=10)

# Crear las etiquetas para mostrar los resultados
winner_label = tk.Label(window, text="")
winner_label.grid(row=2, column=5, columnspan=2, padx=10, pady=10)
team_1_prob_label = tk.Label(window, text="")
team_1_prob_label.grid(row=3, column=5, padx=10, pady=10)
team_2_prob_label = tk.Label(window, text="")
team_2_prob_label.grid(row=3, column=6, padx=10, pady=10)

# Crear la función que se ejecuta cuando se presiona el botón "Calcular"
def calcular_probabilidades():
    team_1_name = team_1_entry.get()
    team_2_name = team_2_entry.get()

    team_1_stats = find_stats(team_1_name)
    team_2_stats = find_stats(team_2_name)
    features = find_features(team_1_stats, team_2_stats)
    probs = gb.predict_proba([features])
    team_1_prob = probs[0][0]
    team_2_prob = probs[0][1]
    if team_1_prob > team_2_prob:
        winner = team_1_name
    elif team_2_prob > team_1_prob:
        winner = team_2_name
    else:
        winner = "Empate"
    result = {
        'team_1': team_1_name,
        'team_2': team_2_name,
        'team_1_prob': round(team_1_prob, 2),
        'team_2_prob': round(team_2_prob, 2),
        'winner': winner
    }
    # Actualizar las etiquetas con los resultados
    winner_label.config(text=f"Ganador: {winner}")
    team_1_prob_label.config(text=f"{team_1_name}: {round(team_1_prob, 2)}")
    team_2_prob_label.config(text=f"{team_2_name}: {round(team_2_prob, 2)}")

    mostrar_bandera()


# Crear el botón "Calcular"
calcular_button = tk.Button(window, text="Calcular", command=calcular_probabilidades)
calcular_button.grid(row=1, column=5, columnspan=2, padx=10, pady=10)

# Crear los labels para mostrar las banderas
bandera_label_1 = tk.Label(window)
bandera_label_1.grid(row=4, column=5)
bandera_label_2 = tk.Label(window)
bandera_label_2.grid(row=4, column=6)


window.mainloop()