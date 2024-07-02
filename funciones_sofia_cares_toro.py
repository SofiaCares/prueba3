import principal_sofia_cares_toro as fn

listaRegistro=[]
listaGif=[]
listaDespachos=[]
listaCobros=[]


while (True):
    print("MENÚ REGALO DE NAVIADAD")
    print("-----------------------")
    print("1.Registro de GIFCARD")
    print("2.Lista GIFCARD")
    print("3.Sector despacho")
    print("4.Salir")
    opcion=int (input("Escoja una opción (1-4): "))

    if (opcion==1):
        print("Registro de Gifcard")
        fn.registrosGIF(listaRegistro)

    if (opcion==2):
        print("Lista de Gifcard")
        fn.gifcard(listaCobros)

    if (opcion==3):
        print("Despacho Gifcard")
        fn.Despachos(listaDespachos)

    if (opcion==4):
        print("¡MENÚ FINALIZADO!")
        break
