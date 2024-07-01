#dicJugador1 = {  "nombre":"luis", "edad":30 }
#dicJugador2 = {  "nombre":"Andres", "edad":26 }
#print(f"nombre:{dicJugador1["nombre"]} edad:{dicJugador1["edad"]}")
#print(dicJugador2["nombre"])
listaPersonas=[]
continuar="S"
while(continuar=="S"):
    nombre = input("ingrese el nombre:")
    edad = int(input("ingrese su edad:"))
    dic = {"nombre":nombre,"edad":edad}
    listaPersonas.append(dic)
    continuar=input("desea continuar(S/N):")
print(listaPersonas)
for i in range( len(listaPersonas)  ):
    print(f"nombre de la persona:{listaPersonas[i]["nombre"]}")
    print(f"edad de la persona:{listaPersonas[i]["edad"]}")
