# 6 ramos
# 6,7  6,8   7   4,5   5,3  2,0
# Ejercicio 1
asignatura=[]
for i in range(6):
    nota=float(input(f"Ingrese nota ramo {i+1}:"))
    asignatura.append(nota)
print(asignatura)

# ejercicio 2
for i in range(6):
    print(asignatura[i])
for i in asignatura:
    print(i)
    
# ejercicio 3