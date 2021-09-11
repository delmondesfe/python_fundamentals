class Pilha:
    def __init__(self):
        self.pilha = []
        self.topo = 0
        self._uso_interno = True
        self.__mangled = True

    def empilhar(self, item):
        self.pilha.append(item)
        self.topo +=1


    def desempilhar(self):
        if not self.valida_pilha():
            item_removido =self.pilha[-1]
            del self.pilha[-1]
            self.topo -=1
            return print('O item {} foi removido'.format(item_removido))
        return print('Pilha esta vazia')
    

    def valida_pilha(self):
        return len(self.pilha)==0



    