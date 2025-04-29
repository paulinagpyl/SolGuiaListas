# 6 ramos
# 6,7  6,8   7   4,5   5,3  2,0
# # Ejercicio 1
# asignatura=[]
# for i in range(6):
#     nota=float(input(f"Ingrese nota ramo {i+1}:"))
#     asignatura.append(nota)
# print(asignatura)

# # ejercicio 2
# for i in range(6):
#     print(asignatura[i])
# for i in asignatura:
#     print(i)
    
# ejercicio 3
# asignatura = [ 6.7,6.8,7,4.5,5.3,2]
# cont=0
# for i in range(len(asignatura)):
#     if asignatura[i]==4.5:
#         cont+=1
# print(f"hay {cont} notas 4.5 es (con range)")
# cont2=0
# for i in asignatura:
#     if i==4.5:
#         cont2+=1
# print(f"hay {cont2} notas 4.5 es (con in)")

#extra encontrar 6,7
asignatura = [ 6.7,6.8,7,4.5,5.3,2]
posicion=0
for i in range(len(asignatura)):
    if asignatura[i] == 6.7:
        posicion=i+1
print(f"el 6,7 esta como nota {posicion}")