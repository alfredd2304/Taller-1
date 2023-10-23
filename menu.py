print("  ")
print("  ")
print("Bienvenido al Restaurante, que deseas hacer?")
print("(Digite numero)")

compra = []
costo_total = 0
i=0
while i==0:
    print("1. Ver Menu")
    print("2. Resumen del Pedido")
    print("3. Eliminar productos")
    print("4. Pagar Pedido")
    print("5. Salir")
    opcion = int(input())
    if opcion==1:
        print(" ")
        print("Ha entrado al Menu, haga su pedido")
        while True:
            print("1. Hamburguesa   ==> 20000$")
            print("2. Papas fritas  ==>  5000$")
            print("3. CocaCola Zero ==>  4000$")
            print("4. Nuggets combo ==> 22000$")
            print("5. Helado grande ==>  7000$")
            print("6. Volver al menu anterior")
            opcion2 = int(input("Digite un numero:"))
            if opcion2 == 1:
                compra.append("Hamburguesa x1 ==>20000$")
                costo_total = costo_total+20000
                print(" ")
                print("Anotado, algo mas?")
                print(" ")
            if opcion2 ==2:
                compra.append("Papas Fritas x1 ==>5000$")
                costo_total = costo_total+5000
                print(" ")
                print("Anotado, algo mas?")
                print(" ")
            if opcion2==3:
                compra.append("CocaCola Zero x1 ==>4000$")
                costo_total = costo_total+4000
                print(" ")
                print("Anotado, algo mas?")
                print(" ")
            if opcion2==4:
                compra.append("Nuggets combo x1 ==>22000$")
                costo_total = costo_total+22000
                print(" ")
                print("Anotado, algo mas?")
                print(" ")
            if opcion2==5:
                compra.append("Helado grande x1 ==>7000$")
                costo_total = costo_total+7000
                print(" ")
                print("Anotado, algo mas?")
                print(" ")
            if opcion2==6:
                print(" ")
                break
            elif opcion2<1 or opcion2>6:
                print("Digite un numero del 1 al 6")

    if opcion == 2:
        if len(compra)==0:
            print("La lista esta vacia")
            print(" ")
        else:
            print(" ")
            print("RESUMEN DEL PEDIDO")
            print(compra)
            print(f"El costo total es {costo_total}$")
            print(" ")
    
    if opcion==3:
        print("")
        print("HA SELECCIONADO ELIMINAR PRODUCTOS")
        print("Por favor escriba el producto que desea eliminar(asegurese de escribirlo igual)")
        print(compra)
        opcion3 = str(input())
        if opcion3==("Hamburguesa"):
                costo_total= costo_total-20000
                compra.remove("Hamburguesa x1 ==>20000$")
                print("Se ha removido la hamburguesa satisfactoriamente")
        elif opcion3==("Papas fritas"):
            costo_total= costo_total-5000
            compra.remove("Papas Fritas x1 ==>5000$")
            print("Se ha removido las Papas Fritas satisfactoriamente")

        elif opcion3==("CocaCola Zero"):
            costo_total= costo_total-4000
            compra.remove("CocaCola Zero x1 ==>4000$")
            print("Se ha removido la CocaCola Zero satisfactoriamente")

        elif opcion3==("Nuggets combo"):
            costo_total= costo_total-22000
            compra.remove("Nuggets combo x1 ==>22000$")
            print("Se han removido los Nuggets combo satisfactoriamente")
        
        elif opcion3==("Helado grande"):
            costo_total= costo_total-7000
            compra.remove("Helado grande x1 ==>7000$")
            print("Se ha removido el Helado grande satisfactoriamente")
        else:
            print("No se elimino ningun producto, asegurese de escribir las mayusculas")
            print("")
        
    if opcion==4:
        print("")
        print(f"Costo total {costo_total}$")
        print("Desea confirmar el pago? s/n")
        respuesta = str(input())
        if respuesta=="s" and compra!=0:
            print("")
            print("Su pago ha sido aprobado...")
            print(compra)
            print(f"precio total: {costo_total}$")
        else:
            print("")
            print("no se ha efectuado la compra")

    if opcion == 5:
        print("Hasta luego")
        i=1

        
   


