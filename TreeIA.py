import Fila
import Pilha

class No:
 
    def __init__(self, valor):
 
        self.info = valor
        self.filhos=[]

    def insere(self, valor1, valor2):
         if valor2 == self.info:
             self.filhos.append(No(valor1))
         else:
             for i in self.filhos:
                 i.insere(valor1,valor2)

    def show1(self):
        noContagem = 0
        f = Fila.Fila()
        f.inserir(self)
        num = int(input('Digite o numero que deseja buscar em largura: '))
        
        while f.estahVazia() != True:
            self = f.getPrim()
            noContagem += 1
            if(num == self.info):
                print("O numero", num, "foi encontrado apos andar: ", noContagem, "nós")
                break
            print(self.info)
            f.remover()
            for i in self.filhos: 
                f.inserir(i)

    def show2(self):
        noContagem = 0
        p = Pilha.Pilha()
        p.push(self)
        num = int(input('Digite o numero que deseja buscar em profundidade: '))
        
        while p.estahVazia() != True:
            self = p.getTopo()
            noContagem += 1
            if(num == self.info):
                print("O numero", num, "foi encontrado apos andar: ", noContagem, "nós")
                break
            print(self.info)
            p.pop()
            for i in self.filhos[::-1]:
                p.push(i)

         
  
class TreeIA:

    def __init__(self):
        self.raiz = None

    def insere(self, valor1,valor2):
        if self.raiz == None:
            self.raiz = No(valor1)
        else:
            self.raiz.insere(valor1,valor2)

    def show1(self):
        if self.raiz!=None:
            self.raiz.show1()

    def show2(self):
        if self.raiz!=None:
            self.raiz.show2()




