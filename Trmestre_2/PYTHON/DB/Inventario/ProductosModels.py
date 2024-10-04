class Producto:
    def __obtener_datos(self, ID, nombre, descripcion, cantidad, precio):
        producto = {}
        producto.setdefault("ID", ID)
        producto.setdefault("Nombre", nombre)
        producto.setdefault("Descripcion", descripcion)
        producto.setdefault("Cantidad", cantidad)
        producto.setdefault("Precio", precio)
        return producto
