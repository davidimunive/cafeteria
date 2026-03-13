from enum import Enum

class Rol(Enum):
    BARISTA = "Barista"
    MESERO = "Mesero"
    GERENTE = "Gerente"


class EstadoPedido(Enum):
    PENDIENTE = "Pendiente"
    PREPARANDO = "Preparando"
    ENTREGADO = "Entregado"
    
class Persona:

    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(self.nombre,"inicio de sesion aprobado")

    def actualizarPerfil(self,nombre,email):
        self.nombre=nombre
        self.email=email
        print("Datos Actualizados")


class Cliente(Persona):

    def __init__(self,idPersona,nombre,email):
        super().__init__(idPersona,nombre,email)
        self.puntosFidelidad=0
        self.historialPedidos=[]

    def realizarPedido(self,pedido):
        self.historialPedidos.append(pedido)
        print("Agregado al historial")

    def consultar_Historial(self):
        print("Historial")
        for p in self.historialPedidos:
            print("Pedido:",p.idPedido,"Total:",p.total)

    def canjear_Puntos(self):
        if self.puntosFidelidad >= 50:
            print("Canjeando puntos")
            self.puntosFidelidad = self.puntosFidelidad - 50
            print("Puntos restantes:",self.puntosFidelidad)
            return
        print("Sin suficientes puntos")


class Empleado(Persona):

    def __init__(self,idPersona,nombre,email,idEmpleado,rol):
        super().__init__(idPersona,nombre,email)
        self.idEmpleado=idEmpleado
        self.rol=rol

    def actualizar_inventario(self,inventario,ingrediente,cantidad):
        print("Actualizando inventario...")
        inventario.reducirStock(ingrediente,cantidad)

    def cambiarEstadoPedido(self,pedido,estado):
        pedido.estado=estado
        print("Estado del pedido cambiado a",estado)


class ProductoBase:

    def __init__(self,idProducto,nombre,precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase


class Bebida(ProductoBase):

    def __init__(self,idProducto,nombre,precioBase,tamanio,temperatura):
        super().__init__(idProducto,nombre,precioBase)
        self.tamanio=tamanio
        self.temperatura=temperatura
        self.modificadores=[]

    def agregarExtra(self,extra):
        print("Agregando extra:",extra)
        self.modificadores.append(extra)

    def calcularPrecioFinal(self):
        precio=self.precioBase
        extras=len(self.modificadores)
        precio=precio+(extras*5)
        print("Precio final bebida:",precio)
        return precio


class Postre(ProductoBase):

    def __init__(self,idProducto,nombre,precioBase,esVegano,sinGluten):
        super().__init__(idProducto,nombre,precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten


class Pedido:

    def __init__(self,idPedido):
        self.idPedido=idPedido
        self.productos=[]
        self.estado=EstadoPedido.PENDIENTE
        self.total=0

    def agregarProducto(self,producto):
        print("Producto agregado al pedido")
        self.productos.append(producto)

    def calcularTotal(self):
        print("Calculando total")
        total=0
        for p in self.productos:
            if type(p)==Bebida:
                total=total+p.calcularPrecioFinal()
            if type(p)==Postre:
                total=total+p.precioBase
        self.total=total
        print("Total del pedido:",total)

    def validarStock(self):
        print("Validando stock")
        for p in self.productos:
            print("Verificando producto:",p.nombre)


class Inventario:

    def __init__(self):
        self.ingredientes={}

    def agregarIngrediente(self,nombre,cantidad):
        print("Se esta agregando el ingrediente:",nombre)
        self.ingredientes[nombre]=cantidad

    def reducirStock(self,nombre,cantidad):

        existe=False

        for ingrediente in self.ingredientes:
            if ingrediente==nombre:
                existe=True

        if existe==False:
            print("No se encontro ingrediente")
            return

        if self.ingredientes[nombre] < cantidad:
            print("No hay suficientes ingredientes")
            return

        self.ingredientes[nombre]=self.ingredientes[nombre]-cantidad
        print("Stock actualizado")

    def notificarFaltante(self,nombre):

        for ingrediente in self.ingredientes:
            if ingrediente==nombre:
                if self.ingredientes[nombre] < 5:
                    print("El ingrediente",nombre,"se está terminando")


