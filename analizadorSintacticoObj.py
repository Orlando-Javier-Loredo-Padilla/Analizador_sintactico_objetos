#from constantes import SIMBOLO
from operator import is_, le

from ClasePila import Pila
from ClasePila import ElementoPila
from ClasePila import Terminal
from ClasePila import NoTerminal
from ClasePila import Estado

def main():
    print("Primer ejemplo: ")
    print("Cadena: hola+mundo")
    primerEjercicio("hola+mundo$")
    print("Segundo ejemplo: ")
    print("a+b+c+d+e+f")
    segundoEjercicio("a+b+c+d+e+f$")

def primerEjercicio(texto):
    pila = Pila()
    pila.push(NoTerminal(ElementoPila.SIMBOLO, "$0"))
    pila.mostrarPila()

    estado = ElementoPila.INICIAL
    d=2
    lexema = ""

    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == ElementoPila.INICIAL):
            if (es_Letra(c) or c == '_'):
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                lexema += c
                pila.push(Terminal(ElementoPila.SIMBOLO, lexema+str(d)))
                d += 1
                estado = ElementoPila.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Pila()
                nuevaPila.push(Estado(ElementoPila.E, "$0E1"))
                nuevaPila.mostrarPila()
            else:
                print("ERROR")
                break

        elif(estado == ElementoPila.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Terminal(ElementoPila.IDENTIFICADOR,lexema+str(d)))
                d+=1
                estado = ElementoPila.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        
        else:
            break
        i += 1


def segundoEjercicio(texto):

    pila = Pila()
    pila.push(NoTerminal(ElementoPila.SIMBOLO, "$0"))
    pila.mostrarPila()

    estado = ElementoPila.INICIAL
    d2 = 2
    d3 = 3
    lexema = ""

    i = 0
    while(i<len(texto)):
        c = texto[i]

        if(estado == ElementoPila.INICIAL):
            if (es_Letra(c) or c == '_'): 
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            elif (c == '+'):
                lexema += c
                pila.push(Terminal(ElementoPila.SIMBOLO, lexema + str(d3)))
                estado = ElementoPila.INICIAL
                lexema = ""
                pila.mostrarPila()
            elif (c == '$'):
                pila.clear()
                nuevaPila = Pila()
                nuevaPila.push(Estado(ElementoPila.E,"$0E1"))
                nuevaPila.mostrarPila()
            else:
                print("ERROR")
                break

        elif(estado == ElementoPila.IDENTIFICADOR):
            if(es_Letra(c) or isReal(c) or c == '_'):
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Terminal (ElementoPila.IDENTIFICADOR,lexema+str(d2)))
                estado = ElementoPila.INICIAL
                lexema = ""
                i -= 1
                pila.mostrarPila()
        i += 1

def isReal(c):
    if (ord(c) >= 48 and ord(c) <= 57):
        return True
    else:
        return False

def es_Letra(c):
    if (((ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95) or ((ord(c)>=97 and ord(c)<=122) or ord(c) == 95)):
        return True
    else:
        return False

main()


