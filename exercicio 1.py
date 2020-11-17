def  leiaInt ():
    numeroInt = (input( "Digite um numero inteiro: " ))
    if numeroInt.isdigit() == True:
        pass
    else :
        numeroInt = 0
    return numeroInt
print(leiaInt())