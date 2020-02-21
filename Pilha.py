class No():

    def __init__(self, valor=None, proximo=None):
        self.info=valor
        self.prox=proximo

class Pilha():

    def __init__(self):
        self.prim = None;
        self.ult = None;
        self.quant = 0;

    def push(self,valor):
        if self.quant==0:
            self.prim = self.ult = No(valor,None)
        else:
            self.prim = No(valor,self.prim)
        self.quant+=1

    def pop(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox;
        self.quant-=1

    def imprimir(self):
        aux = self.prim
        while aux != None:
            print(aux.info)
            aux = aux.prox
        print("\n")

    def getTopo(self):
        return self.prim.info

    def estahVazia(self):
        return self.quant==0


                
            



        
        
