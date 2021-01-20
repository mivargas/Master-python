"""
pedir la nota de 15 alumnos y decir cuantos han aprobado y cuantos reprobado
"""

contador = 1
aprobados = 0
reprobados = 0

numero_alumnos = int( input("¿Cuantos alumnos? ") )

while contador <= numero_alumnos:
    nota = int(input(f"Nota para el alumno {contador} "))
    
    if nota >= 5:
        aprobados+=1
    else:
        reprobados+=1

    contador+=1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
