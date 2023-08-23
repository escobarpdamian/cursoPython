from primer_paquete.modulo1 import Cliente
from primer_paquete.modulo2 import Producto

producto1 = Producto("Yerba",2,2400)

cliente1 = Cliente("Pablo","Escobar","35803089","prueba@pbtw.com.ar")

cliente1.comprar(producto1)
cliente1.ver_ult_compra()
print(cliente1)
print(producto1)