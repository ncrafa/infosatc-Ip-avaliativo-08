

def leiaInt():
      try:
            numeroInt = int(input( "Informe um numero inteiro: " ))
      except:
            print ( "Inválido ! Somente dígito inteiro   " )
      else:
            print("número",numeroInt,"válido")
def  leiafloat ():
      try:
            nfloat = float(input( "Insira um numero decimal: " ))
      except:
            print ( "Ops, número inválido. Apenas número com vírgula é aceito" )
      else:
            print("número",nfloat,"válido")


leiaInt()
leiafloat ()

