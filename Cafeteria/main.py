from models import *
def crear_datos():

    clientes = [
        Cliente(1,"Ana Munive","ana@gmail.com"),
        Cliente(2,"Carlos Munive","carlos@gmail.com"),
        Cliente(3,"Maria Munive","maria@gmail.com"),
        Cliente(4,"Luis Munive","luis@gmail.com"),
        Cliente(5,"Sofia Munive","sofia@gmail.com"),
        Cliente(6,"Pedro Munive","pedro@gmail.com"),
        Cliente(7,"Laura Munive","laura@gmail.com"),
        Cliente(8,"Diego Munive","diego@gmail.com"),
        Cliente(9,"Elena Munive","elena@gmail.com"),
        Cliente(10,"Andres Munive","andres@gmail.com"),
    ]
 
    empleados = [
        Empleado(11,"Roberto Silva","roberto@cafe.com","E001", Rol.BARISTA),
        Empleado(12,"Carmen Diaz","carmen@cafe.com","E002", Rol.MESERO),
        Empleado(13,"Jorge Perez","jorge@cafe.com","E003", Rol.GERENTE),
        Empleado(14,"Patricia Leon","patricia@cafe.com","E004", Rol.BARISTA),
        Empleado(15,"Miguel Rios","miguel@cafe.com","E005", Rol.MESERO),
        Empleado(16,"Isabel Fuentes","isabel@cafe.com","E006", Rol.BARISTA),
        Empleado(17,"Ramon Castro","ramon@cafe.com","E007", Rol.MESERO),
        Empleado(18,"Lucia Pardo","lucia@cafe.com","E008", Rol.GERENTE),
        Empleado(19,"Victor Mora","victor@cafe.com","E009", Rol.BARISTA),
        Empleado(20, "Gloria Nava","gloria@cafe.com","E010", Rol.MESERO),
    ]
 
    bebidas = [
        Bebida(1,"Cappuccino",45.0,"Mediano","Caliente"),
        Bebida(2,"Latte",50.0,"Grande","Caliente"),
        Bebida(3,"Cafe de Olla",35.0,"Chico","Caliente"),
        Bebida(4,"Frappuccino",65.0,"Grande","Fria"),
        Bebida(5,"Matcha Latte",60.0,"Mediano","Caliente"),
        Bebida(6,"Cafe Veracruzano",40.0,"Mediano","Caliente"),
        Bebida(7,"Cold Brew",55.0,"Grande","Fria"),
        Bebida(8,"Espresso",30.0,"Chico","Caliente"),
        Bebida(9,"Chocolate",48.0,"Mediano","Caliente"),
        Bebida(10,"Limonada",42.0,"Grande","Fria"),
    ]
 
    postres = [
        Postre(11, "Camote", 55.0, False, False),
        Postre(12, "Brownie magico",40.0, False, False),
        Postre(13, "Muffin Vegano",45.0, True,  False),
        Postre(14, "Galleta sin Gluten",35.0, False, True),
        Postre(15, "Pay de Manzana",50.0, False, False),
        Postre(16, "Tarta Vegana",60.0, True,  True),
        Postre(17, "Concha",30.0, False, False),
        Postre(18, "Pastel de elote",38.0, False, False),
        Postre(19, "Pastel de Zanahoria",52.0, True, False),
        Postre(20, "Macarron",45.0, False, False),
    ]
 
    inventario = Inventario()
    inventario.agregarIngrediente("leche",50)
    inventario.agregarIngrediente("cafe",40)
    inventario.agregarIngrediente("azucar",30)
    inventario.agregarIngrediente("harina",4)
    inventario.agregarIngrediente("chocolate",20)
    inventario.agregarIngrediente("crema",15)
    inventario.agregarIngrediente("vainilla",3)
    inventario.agregarIngrediente("mantequilla",10)
    inventario.agregarIngrediente("huevo",25)
    inventario.agregarIngrediente("matcha",5)
 
    pedidos = []
    for i in range(10):
        p = Pedido(i + 1)
        p.agregarProducto(bebidas[i])
        p.agregarProducto(postres[i])
        pedidos.append(p)
 
    return clientes, empleados, bebidas, postres, inventario, pedidos
 
def menu_clientes(clientes, pedidos):
    print("\nCLIENTES")
    print("1. Ver todos los clientes")
    print("2. Login")
    print("3. Actualizar perfil")
    print("4. Realizar pedido")
    print("5. Ver historial")
    print("6. Canjear puntos")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[LISTA DE CLIENTES]")
        for c in clientes:
            print(" ", c.nombre, "-", c.email)
 
    elif opcion == "2":
        print("\n[LOGIN CLIENTES]")
        for c in clientes:
            c.login()
 
    elif opcion == "3":
        c = clientes[0]
        print("Antes:", c.nombre, c.email)
        c.actualizarPerfil("Ana Lopez Reyes", "ana_nuevo@email.com")
        print("Despues:", c.nombre, c.email)
 
    elif opcion == "4":
        c = clientes[0]
        c.realizarPedido(pedidos[0])
        print("Pedido realizado por", c.nombre)
 
    elif opcion == "5":
        clientes[1].realizarPedido(pedidos[1])
        clientes[1].realizarPedido(pedidos[2])
        clientes[1].consultar_Historial()
 
    elif opcion == "6":
        c = clientes[0]
        c.puntosFidelidad = 150
        print("Puntos actuales:", c.puntosFidelidad)
        c.canjear_Puntos()
        c.canjear_Puntos()
 
 
def menu_empleados(empleados, inventario, pedidos):
    print("\n--- EMPLEADOS ---")
    print("1. Ver todos los empleados")
    print("2. Login")
    print("3. Actualizar inventario")
    print("4. Cambiar estado de pedido")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[LISTA DE EMPLEADOS]")
        for e in empleados:
            print(" ", e.nombre, "-", e.rol.value)
 
    elif opcion == "2":
        print("\n[LOGIN EMPLEADOS]")
        for e in empleados:
            e.login()
 
    elif opcion == "3":
        e = empleados[0]
        print("Reduciendo stock de leche en 5:")
        e.actualizar_inventario(inventario, "leche", 5)
        print("Stock leche ahora:", inventario.ingredientes["leche"])
 
    elif opcion == "4":
        e = empleados[0]
        p = pedidos[0]
        print("Estado actual:", p.estado)
        e.cambiarEstadoPedido(p, EstadoPedido.PREPARANDO)
        e.cambiarEstadoPedido(p, EstadoPedido.ENTREGADO)
        print("Estado final:", p.estado)
 
 
def menu_bebidas(bebidas):
    print("\n--- BEBIDAS ---")
    print("1. Ver todas las bebidas")
    print("2. Agregar extras")
    print("3. Calcular precio final")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[LISTA DE BEBIDAS]")
        for b in bebidas:
            print(" ", b.nombre, "- $" + str(b.precioBase), "-", b.tamanio, "-", b.temperatura)
 
    elif opcion == "2":
        b = bebidas[0]
        print("Bebida:", b.nombre)
        b.agregarExtra("leche de almendra")
        b.agregarExtra("sin azucar")
        print("Modificadores:", b.modificadores)
 
    elif opcion == "3":
        print("\n[PRECIOS FINALES]")
        for b in bebidas:
            print(" ", b.nombre, "- Precio final: $", b.calcularPrecioFinal())
 
 
def menu_postres(postres):
    print("\nPOSTRES")
    print("1. Ver todos los postres")
    print("2. Ver veganos")
    print("3. Ver sin gluten")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[LISTA DE POSTRES]")
        for p in postres:
            print(" ", p.nombre, "- $" + str(p.precioBase),
                  "- Vegano:", p.esVegano, "- Sin gluten:", p.sinGluten)
 
    elif opcion == "2":
        print("\n[POSTRES VEGANOS]")
        for p in postres:
            if p.esVegano:
                print(" ", p.nombre)
 
    elif opcion == "3":
        print("\n[POSTRES SIN GLUTEN]")
        for p in postres:
            if p.sinGluten:
                print(" ", p.nombre)
 
 
def menu_pedidos(pedidos, clientes, empleados):
    print("\nPEDIDOS")
    print("1. Ver todos los pedidos")
    print("2. Calcular total de un pedido")
    print("3. Validar stock")
    print("4. Flujo completo")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[LISTA DE PEDIDOS]")
        for p in pedidos:
            print(" Pedido:", p.idPedido, "- Estado:", p.estado, "- Productos:", len(p.productos))
 
    elif opcion == "2":
        p = pedidos[0]
        print("Calculando total del pedido", p.idPedido)
        p.calcularTotal()
 
    elif opcion == "3":
        p = pedidos[0]
        p.validarStock()
 
    elif opcion == "4":
        print("\nFLUJO COMPLETO")
        c = clientes[0]
        e = empleados[0]
        p = pedidos[0]
 
        c.login()
        e.login()
        p.calcularTotal()
        e.cambiarEstadoPedido(p, EstadoPedido.PREPARANDO)
        e.cambiarEstadoPedido(p, EstadoPedido.ENTREGADO)
        c.realizarPedido(p)
        c.consultar_Historial()
 
 
def menu_inventario(inventario):
    print("\nINVENTARIO")
    print("1. Ver inventario")
    print("2. Reducir stock")
    print("3. Notificar faltante")
    print("0. Volver")
    opcion = input("Opcion: ")
 
    if opcion == "1":
        print("\n[INVENTARIO ACTUAL]")
        for nombre, cantidad in inventario.ingredientes.items():
            print(" ", nombre, ":", cantidad)
 
    elif opcion == "2":
        print(inventario.reducirStock("leche", 5))
        print(inventario.reducirStock("cafe", 999))
        print(inventario.reducirStock("canela", 2))
 
    elif opcion == "3":
        print("\n[VERIFICANDO FALTANTES]")
        for nombre in inventario.ingredientes:
            inventario.notificarFaltante(nombre)
 
def main():
    clientes, empleados, bebidas, postres, inventario, pedidos = crear_datos()
 
    while True:
        print("\n" + "="*40)
        print("   CAFETERIA - MENU PRINCIPAL")
        print("="*40)
        print("1. Clientes")
        print("2. Empleados")
        print("3. Bebidas")
        print("4. Postres")
        print("5. Inventario")
        print("6. Pedidos")
        print("0. Salir")
        print("="*40)
        opcion = input("Selecciona una opcion: ")
 
        if opcion == "1":
            menu_clientes(clientes, pedidos)
        elif opcion == "2":
            menu_empleados(empleados, inventario, pedidos)
        elif opcion == "3":
            menu_bebidas(bebidas)
        elif opcion == "4":
            menu_postres(postres)
        elif opcion == "5":
            menu_inventario(inventario)
        elif opcion == "6":
            menu_pedidos(pedidos, clientes, empleados)
        elif opcion == "0":
            print("Hasta luego!")
            break
        else:
            print("Opcion no valida.")
 
main()