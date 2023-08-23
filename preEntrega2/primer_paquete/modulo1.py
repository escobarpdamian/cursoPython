class Cliente:
    def __init__(self, nombre, apellido, dni, contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.contacto = contacto

    def __str__(self):
        return f"Soy una instancia de Cliente cuyo nombre es: {self.nombre}"

    def comprar(self, producto):
        self.producto = producto
        print(f"Compraste {producto.nombre} x {producto.cantidad}")
        print(f"por un total de {producto.total()}")

    def ver_ult_compra(self):
        print(f"Tu ultima comprá fué {self.producto.cantidad} x {self.producto.nombre}")