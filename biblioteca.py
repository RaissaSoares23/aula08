def imprimirNome(nome):
    print(f"Nome:{nome}")

def piramide (n):
    for x in range(1, n + 1):
        for y in range(0, x):
            print(x, end=" ")
        print()

def contaVogais(texto):
    cont=0
    for x in range (len(texto)):
        if texto[x]== "a" or texto[x]=="e" or texto[x]== "i" or texto[x]== "o"or texto[x]== "u":
         cont=cont +1
    print (cont)

def estoque(produto, quantidade , valorUnitario):
    valorTotal = quantidade*valorUnitario
    return valorTotal

def numeros(n):
    if n==0:
        return "Z"
    elif n>0:
        return "P"
    else:
        return"N"

def soma (*b):
    res=a+b
    print(res)