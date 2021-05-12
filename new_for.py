activos = [ 
	("ES", 0.25, 50, "US"), 
	("NQ", 0.25, 20, "US"),
	("GC", 0.10, 100, "US"),
	("DAX", 0.50, 50, "EUR")
]

for activo, tick, costo_punto, moneda in activos:
	print("El costo de cada punto em el {} es de {} {} y su minimo desplazamiento es de {} pts.".
		format(activo, costo_punto, moneda, tick))