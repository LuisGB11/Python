import math
#programa 6
def SumaLista(x):      
        lista=[(conta**3)
        for conta in range(1,x+1)]       
        print lista
        return sum(lista)



#programa 7:
def MayorLista(x):
        lista=[(conta**2)
        for conta in range(1,x+1)]        
        num=1
        while num<len(lista):
                if lista[num]>100:
                        print lista[num]
                num+=1


#programa 8:
def MayorN (x):
        conta=1
        while conta<=x:
                if conta>=20 and conta<=60:
                        print conta
                conta+=1


#Programa 9:       
def Hipotenusa (x, y):
        return math.sqrt(x**2 + y**2)

#programa 10:
def recursividad (num, var=0):
        if(num>=0):
                var+=num**2
                return recursividad(num-1,var)
        else:
                print var
