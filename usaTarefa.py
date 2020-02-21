import TreeIA

t = TreeIA.TreeIA()


t.insere(5,6)
t.insere(4,5)
t.insere(3,5)
t.insere(6,5)
t.insere(7,4)
t.insere(8,3)
t.insere(9,7)
t.insere(10,1)

print('Busca em Largura com a contagem dos nós andados ate encontrar o valor: ')
t.show1()

print('-------------------------------------------------------------------------------')

print('Busca em Profundidade com a contagem dos nós andados ate encontrar o valor: ')
t.show2()
