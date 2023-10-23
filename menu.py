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
            opcion2 = int(input())
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
            else:
                print("Digite un numero del 1 al 6")

    if opcion == 5:
        print("Hasta luego")
        i=1

        
   


