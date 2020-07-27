binario = []
listaAstr = ""

def listadeint_a_str(x):
    #En este caso se recibirá una lista de int, por lo que se pasa a str. El trucazo de abajo lo busqué.
    listaAstr = ""
    x = [str(i) for i in x]
    return listaAstr.join(x)

def dedecimal_abinario(x):
    binario = []
    while x // 2 > 0:
        resto = x % 2
        binario.append(str(resto))
        x = x // 2
    if not x % 2 == 0:
        binario.append(1)
    return int(listadeint_a_str(binario[::-1]))

rec = "Escribe tu número en decimal:"
resu = "Tu número en binario es: "
agrad = "Gracias por usar este programirijillo."
firma = "Created by jdelvalle2002 and sponsored by CS42."

print(rec)
decimal = int(input())
print(resu + str(dedecimal_abinario(decimal)))
print(agrad)
print(firma)
