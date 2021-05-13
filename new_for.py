from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import socket


def check_no_network():
	"""Returns True if it fails to reslove broker's URL, False otherwise"""
	try:
		socket.gethostbyneme("https://www.binance.com")
		return False
	except:
		return True

def f_NQ():
	print("This a NQ function")

def f_ES():
	print("Here is a ES momment")

def f_CL():
	print("Reciently the inventary has become simple new")

def f_GC():
	print("This asset is similar to the oil future")

def f_DAX():
	print("When I was a child, I realy loved it")


# for by a lyst of funvtions
def recta(x):
	return x

def main():
	activos = [ 
		("ES", 0.25, 50, "US"), 
		("NQ", 0.25, 20, "US"),
		("CL", 0.10, 100, "US"),
		("GC", 0.10, 100, "US"),
		("DAX", 0.50, 50, "EUR")
	]

	for activo, tick, costo_punto, moneda in activos:
		print("El costo de cada punto en el futuro del {} es de {} {} y su minimo desplazamiento es de {} pts.".
			format(activo, costo_punto, moneda, tick))

	f_list = [
		(f_NQ, "Nasdaq"),
		(f_ES, "S&P_500"),
		(f_GC, "Gold")] 

	for f_ , msg  in f_list:
		
		print("\n"+ msg + " Estamos mandado a llamar la función, esto es magico")
		f_()

	interact(recta, x = 10)



main()