# main.py
from mi_clase import Misterio
from claseAlumno import Alumno

jugador = input("Ingresa tu nombre: ")
juego = Misterio(jugador)
print(juego.resolver())

alumno = Alumno()

registro_alumnos = { }

#Capturar tres registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre(input("Introduce el nombre: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el número de control del alumno: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

#Mostrar los nombres de los registros
for i in range(3):
    print(f"Nombre: {registro_alumnos[i].get_nombre()}")


