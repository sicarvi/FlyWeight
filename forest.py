class TipoArbol:

    def __init__(self, nombre: str, color: str, textura: str):
        self.nombre = nombre
        self.color = color
        self.textura = textura

    def __str__(self):
        nombre = self.nombre
        color = self.color
        texture = self.textura
        texto = f"[Nombre: {nombre}, Color: {color}, Textura: {texture}]"
        return texto

class Arbol:

    def __init__(self,x: int, y: int, tipo: TipoArbol):
        self.x = x
        self.y = y
        self.tipo = tipo


class FabricaDeArboles:

    _tiposPosibles = []

    def mostrarTiposPosibles(self):
        for tipo in self._tiposPosibles:
            print(tipo)

    def ingresarTipo(self, nombre, color, textura):
        objtipo = TipoArbol(nombre, color, textura)
        self._tiposPosibles.append(objtipo)

    def getTipo(self, nombre, color, textura):

        for tipo in self._tiposPosibles:
            if tipo.nombre == nombre and tipo.color == color and tipo.textura == textura:
                print('Reutilizando un tipo de arbol ya existente')
                return tipo

        #No encontró un tipo que coincidiera, hay que crear uno nuevo
        objtipo = TipoArbol(nombre, color, textura)
        self._tiposPosibles.append(objtipo)
        print('Creando un tipo de arbol nuevo')
        self.mostrarTiposPosibles()
        return objtipo


class Bosque:

    arboles = []
    fabricaA = FabricaDeArboles()

    def plantarArbol(self, x, y, nombre, color, textura):

        tipo = self.fabricaA.getTipo(nombre, color, textura)
        arbol = Arbol(x, y, tipo)
        self.arboles.append(arbol)

    def mostrarArboles(self):
        for arbol in self.arboles:
            print(f"Coordenadas->({arbol.x}, {arbol.y}) / Tipo->{arbol.tipo}")

