
class RegistroProducto:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        precio_venta = round(costo / (1 - margen_de_venta),2)
        producto = {
            'id': id,
            'nombre': nombre,
            'descripcion': descripcion,
            'costo': costo,
            'cantidad': cantidad,
            'precio_venta': precio_venta
        }
        self.productos[id] = producto

    def imprimir_productos(self):
        print("Listado de productos:")
        for id, producto in self.productos.items():
            print(f"ID: {id}, Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, "
                  f"Costo: {producto['costo']}, Cantidad: {producto['cantidad']}, Precio de Venta: {producto['precio_venta']}")


registro = RegistroProducto()
registro.registrar_producto(1, 'Manzana', 'Fruta', 10.0, 50, 0.2)
registro.registrar_producto(2, 'Lechuga', 'Vegetal', 15.0, 30, 0.15)
registro.imprimir_productos()
