# limpia_conflictos.py
input_file = "TP1.ipynb"
output_file = "TP1_limpio.ipynb"

with open(input_file, "r", encoding="utf-8") as f:
    lineas = f.readlines()

limpias = []
for linea in lineas:
    if not (linea.startswith("<<<<<<<") or linea.startswith("=======") or linea.startswith(">>>>>>>")):
        limpias.append(linea)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(limpias)

print("Archivo limpio guardado como:", output_file)
