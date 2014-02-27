

def obtener_input():
	return raw_input("Ingrese su programa en brainfuck\n")

def procesar_input(entrada):
	array = [0]*30
	index = 0
	for x in entrada:
		if x == '>':
			if index != 29:
				index+=1
		elif x == '<':
			if index != 0:
				index-=1
		elif x == '+':
			array[index]+=1
		elif x == '-':
			if array[index] != 0:
				array[index]-=1
		else:
			#lanzar error
			pass
	print index
	print printear_array(array)

def printear_array(array):
	index = 0
	for x in range(0, len(array)):
		if array[x] != 0:
			index = x
	return array[0:index+1]


if __name__ == '__main__':
	while True:
		procesar_input(obtener_input())
