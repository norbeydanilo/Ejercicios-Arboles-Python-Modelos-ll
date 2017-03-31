class Nodo_nario():
    def __init__(self, valor, hijos = []):
        self.valor= valor
        self.hijos= hijos

def busqueda(arbol, valor, hijo):
    if arbol.valor == valor:
        return retornoHijos(arbol, 0)
    else:
        if len(arbol.hijos) == hijo + 1 :
            return busqueda(arbol.hijos[hijo], valor, 0)
        elif arbol.hijos == []:
            return []
        else:
            return busqueda(arbol.hijos[hijo], valor, 0) + busqueda(arbol, valor, hijo + 1)

def retornoHijos(arbol, hijo):
    if len(arbol.hijos) == hijo + 1 :
        return retornoHijos(arbol.hijos[hijo], 0)
    elif arbol.hijos == []:
        return [arbol.valor]
    else:
        return retornoHijos(arbol.hijos[hijo], 0) + retornoHijos(arbol, hijo + 1)


a = Nodo_nario('a',[(Nodo_nario('ar',[Nodo_nario('arb',[Nodo_nario('arbo',[Nodo_nario('arbol')])]),Nodo_nario('arr',[Nodo_nario('arro',[Nodo_nario('arroz')])])])),(Nodo_nario('av',[Nodo_nario('avi',[Nodo_nario('avio',[Nodo_nario('avion')])])])),(Nodo_nario('al',[Nodo_nario('alc',[Nodo_nario('alce')]),Nodo_nario('alm',[Nodo_nario('alma')])])),(Nodo_nario('ap',[Nodo_nario('apr',[Nodo_nario('apre',[Nodo_nario('aprec')])]),Nodo_nario('apu',[Nodo_nario('apur',[Nodo_nario('apure')])])])),(Nodo_nario('am',[Nodo_nario('amo',[Nodo_nario('amor')]),Nodo_nario('ama',[Nodo_nario('amar',[Nodo_nario('amart',[Nodo_nario('amarte')])])])]))])
e = Nodo_nario('e',[(Nodo_nario('el',[Nodo_nario('elo',[Nodo_nario('elot',[Nodo_nario('elote')])]),Nodo_nario('ell',[Nodo_nario('ello',[Nodo_nario('ellos')])])])),(Nodo_nario('ec',[Nodo_nario('ech',[Nodo_nario('echa',[Nodo_nario('echar')])])])),(Nodo_nario('ed',[Nodo_nario('eda',[Nodo_nario('edad')]),Nodo_nario('edi',[Nodo_nario('edil')])])),(Nodo_nario('ej',[Nodo_nario('eji',[Nodo_nario('ejid',[Nodo_nario('ejido')])]),Nodo_nario('ejo',[Nodo_nario('ejot',[Nodo_nario('ejote')])])])),(Nodo_nario('em',[Nodo_nario('emi',[Nodo_nario('emir')]),Nodo_nario('emb',[Nodo_nario('embu',[Nodo_nario('embud',[Nodo_nario('embudo')])])])]))])
i = Nodo_nario('i',[(Nodo_nario('il',[Nodo_nario('ile',[Nodo_nario('iles',[Nodo_nario('ileso')])]),Nodo_nario('ili',[Nodo_nario('ilio',[Nodo_nario('ilion')])])])),(Nodo_nario('ig',[Nodo_nario('igu',[Nodo_nario('igua',[Nodo_nario('igual')])])])),(Nodo_nario('im',[Nodo_nario('ima',[Nodo_nario('iman')]),Nodo_nario('imp',[Nodo_nario('impa',[Nodo_nario('impar')])])])),(Nodo_nario('in',[Nodo_nario('ing',[Nodo_nario('ingl',[Nodo_nario('ingles')])]),Nodo_nario('int',[Nodo_nario('inte',[Nodo_nario('inter')])])])),(Nodo_nario('is',[Nodo_nario('isl',[Nodo_nario('isla')]),Nodo_nario('isr',[Nodo_nario('isra',[Nodo_nario('israe',[Nodo_nario('israel')])])])]))])
o = Nodo_nario('o',[(Nodo_nario('ob',[Nodo_nario('obo',[Nodo_nario('obol',[Nodo_nario('obolo')])]),Nodo_nario('obr',[Nodo_nario('obra',[Nodo_nario('obrar')])])])),(Nodo_nario('oz',[Nodo_nario('ozo',[Nodo_nario('ozon',[Nodo_nario('ozono')])])])),(Nodo_nario('ov',[Nodo_nario('ova',[Nodo_nario('oval')]),Nodo_nario('ove',[Nodo_nario('ovej',[Nodo_nario('oveja')])])])),(Nodo_nario('or',[Nodo_nario('ord',[Nodo_nario('orde',[Nodo_nario('orden')])]),Nodo_nario('ore',[Nodo_nario('orej',[Nodo_nario('oreja')])])])),(Nodo_nario('ol',[Nodo_nario('olo',[Nodo_nario('olor')]),Nodo_nario('olv',[Nodo_nario('olvi',[Nodo_nario('olvid',[Nodo_nario('olvido')])])])]))])
u = Nodo_nario('u',[(Nodo_nario('ul',[Nodo_nario('ule',[Nodo_nario('ulem',[Nodo_nario('ulema')])]),Nodo_nario('ule',[Nodo_nario('ulen',[Nodo_nario('uleno')])])])),(Nodo_nario('ue',[Nodo_nario('ues',[Nodo_nario('uest',[Nodo_nario('ueste')])])])),(Nodo_nario('ur',[Nodo_nario('urb',[Nodo_nario('urbe')]),Nodo_nario('urg',[Nodo_nario('urgi',[Nodo_nario('urgir')])])])),(Nodo_nario('um',[Nodo_nario('umb',[Nodo_nario('umbr',[Nodo_nario('umbra')])]),Nodo_nario('ume',[Nodo_nario('umer',[Nodo_nario('umero')])])])),(Nodo_nario('ub',[Nodo_nario('ubr',[Nodo_nario('ubre')]),Nodo_nario('ubi',[Nodo_nario('ubic',[Nodo_nario('ubica',[Nodo_nario('ubicar')])])])]))])



print("----------------------------------------------------------------------------------")
print(busqueda(a,"ar",0))
print(busqueda(e,"el",0))
print(busqueda(i,"il",0))
print(busqueda(o,"ob",0))
print(busqueda(u,"ul",0))



