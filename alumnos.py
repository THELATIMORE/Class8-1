def alumnos():
    alumnos = []
    respuesta = True

    while respuesta:
        alumno = []

        alumno.append(input("ingrese el nombre del alumno:\n"))
        alumno.append(float(input("ingrese la primera nota:\n")))
        alumno.append(float(input("ingrese la segunda nota:\n")))
        alumno.append(float(input("ingrese la tercera nota:\n")))

        alumnos.append(alumno)

        respuesta = input("Desea ingresar otro alumno?\nIngrese s para si.\nde lo contrasio ingrese N")
        if respuesta == "s":
            respuesta = True
        else:
            respuesta = False



    if len(alumnos) >0:
        print("lista de las notas de alumnos")
        print("nombre\tnota1\tnota2\tnota3")
        for alumno in alumnos:
            print(alumno[0]+ "\t"+str(alumno[1])+"\t\t"+str(alumno[2])+"\t\t"+str(alumno[3]))

    if len(alumno) > 0:
        print("\nlistado de los promedios de alumnos")
        print("nombre\tpromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            if promedio < 3 :
                print(alumno[0]+"\t"+str(round(promedio,1)))

    if len(alumno) > 0:
        print("\nlistado de alumnos que perdieron la materia")
        print("nombre\tpromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])/3
            if promedio < 3:
                print(alumno[0]+"\t"+str(round(promedio,1)))