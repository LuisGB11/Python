def media(x,y,z):
        med = (float(x+y+z)/float(3))
        print med
        print " "
        
def volumen(radio):
        vol = (1.33*3.1416)*(float(radio**3))
        print vol
        print " "

def impar (num):
	while num <= 32:
		print num
		num += 2
	print " "
		
def mayornum(x,y,z):
        if x>y and x>z:
                print "mayor",x
        elif y>x and y>z:
                print "mayor",y
        elif z>x and z>y:
                print "mayor",z
        print " "
                
def rotar(lista):
	lista.append(lista[0])
	lista.remove(lista[0])
	print lista
	print " "
def rotardos(lista):
        lista.reverse()
        print lista
        print ""

def listas():
        print " 0.- Media"
        print " 1.- Volumen esfera"
        print " 2.- Impares"
        print " 3.- Numero Mayor"
        print " 4.- Rotar Lista"
        print " 5.- salir"
        num = input("Seleccione una opcion ")
        print " "
        if num==0:
                media((input("Ingrese un valor ")),(input("Ingrese un valor ")),(input("Ingrese un valor ")))
                listas()
        elif num == 1:
                volumen(input("Ingrese el Radio:  "))
                listas()
        if num==2:
                impar(13)
                listas()
        elif num == 3:
                mayornum(input("Ingrese numero  "),input("Ingrese numero  "),input("Ingrese numero  "))
                listas()
        elif num == 4:
                rotardos(input("Ingrese vector "))
                listas()
                
        elif num == 5:
                exit()
listas()

