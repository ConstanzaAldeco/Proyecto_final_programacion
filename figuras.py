def  rectangulo (base, altura):
	area=base*altura
	perimetro=2*(base+altura)
	return  area, perimetro
def triangulo (base, altura):
	area=base*altura/2
	perimetro=base+2*altura
	return area, perimetro
def circulo (radio):
	area=3.14159(radio**2)
	perimetro= 2*3.14159*radio
	return area, perimetro

