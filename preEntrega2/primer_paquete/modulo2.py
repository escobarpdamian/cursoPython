class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Soy el producto {self.nombre}"

    def total(self):
        return int(self.cantidad) * int(self.precio)
    