class Node():
    def __init__(self, parent=None, pos=None):
        self.parent = parent
        self.position = pos
        
        #f: custo total do nó
        self.f = 0
        #g: distância do nó atual para o nó inicial 
        self.g = 0
        #h: distância estimada do nó atual para o nó final
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position