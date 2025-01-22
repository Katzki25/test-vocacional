from random import randint
preguntas=[]
for i in range(0,80):
    preguntas.append(0)

areas=[[4,9,12,20,28,31,35,39,43,46,50,65,67,68,75,77],
       [6,13,23,25,34,37,38,42,49,52,55,63,66,70,72,78],
       [5,10,15,19,21,26,29,33,36,44,53,56,59,62,71,80],
       [1,7,11,17,18,24,30,41,48,51,58,60,61,64,73,79],
       [2,3,8,14,16,22,27,32,40,45,47,54,57,69,74,76]]
print("testvocacional\ncomprobaciondeltest")
for area in areas:
    print("%d" % len(area))

print("%d" % len(preguntas))

print("cuestionario")
for i in range(0,len (preguntas)):
    #r=randint(0,1)
    r=int (input("pregunta %d. me interesa 1/ no me interesa 0" % (i+1)))
    #print("%d" % r)
    preguntas[i] = r 

print("respuestas")
for respuesta in preguntas:
    print("%d" % respuesta)

print("procesando")
resultados = [0,0,0,0,0]

i=0
for area in areas:
    for pregunta in area:
        for respuesta in range(0,len (preguntas)):
            if (preguntas[respuesta] == 1 and respuesta == pregunta):
                resultados[i]+=1
    i+=1

for resultado in resultados:
    print("%d" % resultado)
  
    