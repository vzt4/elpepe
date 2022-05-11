#P1-----------------------------------------------------------------------------------------

poto = str(input())
poto1 = str(input())

print(poto1[len(poto)])

#P2-----------------------------------------------------------------------------------------

def adivina(guia,test):
    palabra = ''

    for letra in guia:
        if letra in test:
            palabra += letra

    if palabra == guia:
        return True
    
    return False

guia = str(input())
test1 = str(input())
test2 = str(input())
test3 = str(input())

print(adivina(guia,test1))
print(adivina(guia,test2))
print(adivina(guia,test3))

#P3-----------------------------------------------------------------------------------------

def ambos(txt):
    for caracter in txt:
        if caracter not in 'QWERTYUIOPASDFGHJKLZXCVBNM0123456789qwertyuiopasdfghjklzxcvbnm':
            return False
    return True

def solo_minus(txt): # Ver si esta solo en minuscula
    for caracter in txt:
        if caracter not in 'qwertyuiopasdfghjklzxcvbnm1234567890':
            return False
    return True

def solo_mayus(txt): # Ver si esta solo en mayuscula
    for caracter in txt:
        if caracter not in 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890':
            return False
    return True

a = input()


if solo_mayus(a):
    print(a.lower())
    
elif solo_minus(a):
    print(a.upper())

elif ambos(a):
    print(a)

else:
    print("01111001 01100001")
    
#P4-----------------------------------------------------------------------------------------

def elpepe(txt,num):

    p1 = txt[:num]
    p2 = txt[num:]
    
    nueva_palabra = p2 + p1
    
    print(nueva_palabra)
    
palabra = str(input())
numero = int(input())

elpepe(palabra,numero)

#P5-----------------------------------------------------------------------------------------

def sacar_consonantes(txt):
	
	nueva = ''

	for caracter in txt:
		#Ver si es una vocal
		if caracter not in 'aeiouAEIOU':
			
			if caracter != ' ':
				nueva += ''
			else:
				nueva += ' '
		else:
			nueva += caracter
		
	return print(nueva)

a = str(input())

sacar_consonantes(a)

#P6-----------------------------------------------------------------------------------------

# Ver donde hay comas o puntos
# Sacar su posicion
# Cortar la frase entre 
def cortar(txt):
	
	pc = []
	
	for pos in range(0,len(txt)):
		if txt[pos] in ',.':
			pc.append(pos)
	
	return pc

a = str(input())

pos = cortar(a)

primero = pos[0]
ultimo = pos[1]

print(a[primero+1:ultimo])
print('posiciones',primero,'-',ultimo)

#P7-----------------------------------------------------------------------------------------

def pts(txt): # Ver donde estan los ':'
	for pos in range(0,len(txt)):
		if txt[pos] == ':':
			return pos 

def adivina(guia,test): # Comparar las frases para ver si esta el 'yo no fui'
    
    if guia in test:
        return True
    return False

def sus(txt): # Ver si es el sus :o 
	pos = pts(txt)
	nombre = txt[ : pos ]
	mensaje = txt[ pos + 1 : ]
	if adivina('yo no fui',mensaje):
		return nombre
	return 'nao nao'

# Primera parte :))	
n_msg = int(input())

for msg in range(n_msg):
	a = str(input())
	if sus(a) != 'nao nao':
		impostor = sus(a) 

def pasillo(txt): # Ver el pasillo donde estaba el sus :o
	xd = ''
	for caracter in txt:
		if caracter in '0123456789':
			xd += caracter
	return xd	
	
# Segunda parte :))
n_msg = int(input())

for msg in range(n_msg):
	a = str(input())
	
	pos = pts(a)
	mensaje = a[ pos + 1 : ] 
	
	if adivina(impostor,mensaje):
		pasillo = pasillo(mensaje) # EL PASILLO

# Tercera parte :((

caida = str(input())

contador = 0
maximo_t = 0
posicion = 0
pos_m = 0

for caracter in caida: # Ver la duracion de las desconexiones 
    
    if caracter == 'F':
        contador += 1 #contador=4

    elif caracter == 'D':
        contador = 0
    
    maximo = contador
    
    if maximo > maximo_t: # Ver la MAXIMA desconexion
        maximo_t = maximo
        pos_m = posicion
        
        if caida[pos_m:pos_m+1] == 'F':
            pos_m += 1
            
    posicion += 1
        


print('Impostor:',impostor)
print('Ultima posicion: Pasillo',pasillo)
print('La desconexion mas larga duro',maximo_t,'minutos y comenzo al minuto',pos_m-maximo_t)

#P8-----------------------------------------------------------------------------------------

#AUN NO TA :)))

    
