print("Bienvenide al copiador de archivos .txt")
text = input("Inserta el nombre de tu archivo (incluyendo extension):\n")

nombre = input("Inserta el nombre del nuevo archivo (incluyendo extension):\n")
# nuevo objetivo: añadir q restrinja si no está bien la ext
new = open(nombre, "w")
#recuerda sacar luego el archivo de la carpeta
old = open(text)
o = old.readlines()
for line in o:
    new.write(line)

old.close()
new.close()
print("Tu archivo",text, "fue copiado a", nombre, "exitosamente")