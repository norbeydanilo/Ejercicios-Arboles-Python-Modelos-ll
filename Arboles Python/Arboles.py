class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der

def inorden(arbol):
    if arbol==None:
        return []
    else:
        return inorden(arbol.izquierda) + [arbol.valor] + inorden(arbol.derecha)

def buscar(arbol,valor):
    if arbol==None:
        return False
    elif arbol.valor==valor:
        return True
    else:
        return buscar(arbol.izquierda,valor) or buscar(arbol.derecha,valor)

def evaluar(arbol):
    if arbol.valor=='+':
        return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
    elif arbol.valor=='-':
        return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
    else:
        return int(arbol.valor)

def preorden(arbol):
    if arbol==None:
        return " "
    else:
        return arbol.valor + preorden(arbol.izquierda) + preorden(arbol.derecha)

def posorden(arbol):
    if arbol==None:
        return " "
    else:
        return posorden(arbol.izquierda) + posorden(arbol.derecha)+ arbol.valor
    
def buscarOrdenado(arbol,valor):
    if arbol==None:
        
        return False
    elif arbol.valor==valor:
        
        return True
    elif valor<arbol.valor:
       
        return buscarOrdenado(arbol.izquierda,valor)
    elif valor>arbol.valor:
       
        return buscarOrdenado(arbol.derecha,valor)
        
def insertar(arbol,valor):
    if arbol==None:
        return Nodo(valor)
    elif valor<arbol.valor:
        return Nodo(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    elif valor>arbol.valor:
        return Nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))
        


    
print(inorden(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))

print(buscar(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6'))),'8'))

print(evaluar(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))

print(preorden(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))

print(posorden(Nodo('+',Nodo('5'),Nodo('-',Nodo('8'),Nodo('6')))))

print(buscarOrdenado(Nodo(10,Nodo(5),Nodo(20,Nodo(15),Nodo(25))),20))

print(inorden(insertar(Nodo(10,Nodo(5),Nodo(20,Nodo(15),Nodo(25))),27)))




    
        
