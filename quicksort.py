def quicksort(lista):
	if len(lista) <=1:
		return lista
	pivot = lista[0]
	lista1 = []
	lista2 = []
	for i in lista[1:]:
		if i <= pivot:
			lista1.append(i)
		else:
			lista2.append(i)
	return quicksort(lista1) + [pivot] + quicksort(lista2)

lista = [0,2,0,6,4,3,6,7,8,9,31,23,42,11,3,4,2,1,6,5,4,3,7,8]

# print quicksort(lista)[::-1] # ordina la lista dal piu grande al piu piccolo
print quicksort(lista)
