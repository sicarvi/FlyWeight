from forest import Bosque, FabricaDeArboles



if __name__ == '__main__':
    bosque = Bosque()
    fabrica = FabricaDeArboles()

    fabrica.ingresarTipo('guayabo', 'verde', 'rugoso')
    fabrica.ingresarTipo('cerezo', 'rosado', 'liso')
    fabrica.ingresarTipo('pino', 'verde', 'aspero')

    bosque.plantarArbol(15, 45, 'guayabo', 'verde', 'rugoso')
    bosque.mostrarArboles()

    bosque.plantarArbol(10, 70, 'algarrobo', 'verde', 'rugoso')
    bosque.mostrarArboles()
    #print('--------------------------------------------')
    #fabrica.mostrarTiposPosibles()

