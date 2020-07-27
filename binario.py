def debinarioanormal(x):
    num = 0
    dig = list(x)
    digbien = dig[::-1]
    posiciones = (range(len(dig)))
    for pos in posiciones:
        if int(digbien[pos]) == 1:
            num += 2 ** pos
        elif int(digbien[pos]) == 0:
            num = num
        else:
            num = " Eso no es binario *facepalm*"
            break
    return num

rec = "Escribe tu número en binario:"
resu = "Tu número normalito es... :"
agrad = "Gracias por usar este programirijillo."
firma = "Created by jdelvalle2002 and sponsored by CS42."
print(rec)
numbin = input()
print(resu + str(debinarioanormal(numbin)))
print(agrad)
print(firma)