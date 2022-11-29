def desempeño_aual(nombre_archivo,equipo,año):
    archivo=open(nombre_archivo,"r")
    vacio=[]
    for añadir in archivo:
        añadir=añadir.strip().split(",")
        vacio.append(añadir)
    archivo.close()
    nombre=equipo+"-"+str(año)+".txt"
    comps=open(nombre,"a")
    vacio[0].sort()
    contador=0
    for fecha,equipo1,goles_equipo1,equipo2,goles_equipo2 in vacio:
        if str(año) in fecha and equipo in equipo1 or equipo in equipo2 and str(año) in fecha:
            if equipo2 == equipo:
                reemplazo1=equipo2
                reemplazo2=equipo1
                equipo2=reemplazo2
                equipo1=reemplazo1
                reemplazo3=goles_equipo2
                reemplazo4=goles_equipo1
                goles_equipo2=reemplazo4
                goles_equipo1=reemplazo3
            if int(goles_equipo1)>int(goles_equipo2):
                comps.write(fecha+" contra "+equipo2+","+" victoria: "+goles_equipo1+" a "+goles_equipo2)
                contador += 1
            if int(goles_equipo1)<int(goles_equipo2):
                comps.write(fecha + " contra " + equipo2 + "," + " derrota: " + goles_equipo1 + " a " + goles_equipo2)
                contador += 1
            if int(goles_equipo1) == int(goles_equipo2):
                comps.write(fecha + " contra " + equipo2 + "," + " empate: " + goles_equipo1 + " a " + goles_equipo2)
                contador+=1
            comps.write("\n")

    return contador
print(desempeño_aual("resultados.txt","Chile",2010))