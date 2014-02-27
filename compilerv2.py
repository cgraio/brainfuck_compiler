def splitear(entrada):
	primer_corchete = entrada.find('[')
	if primer_corchete == -1:
		return [entrada]
	bloques_codigo = [entrada[0 : primer_corchete]]
	xxx = obtener_siguiente_bloque(entrada[primer_corchete:])
	return bloques_codigo.append(entrada[primer_corchete : xxx]) + splitear(entrada[xxx:])


def procesar_input_con_split(entrada_spliteada):
	for x in entrada_spliteada:
		procesar_input(x)
