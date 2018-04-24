def max(lista):

    if len(lista)==1:
        return lista[0]

    submax = max(lista[1:])

    if lista[0] > submax:

        return lista[0]

    else:

        return submax

lista = [-1,5,9]
print(max(lista))