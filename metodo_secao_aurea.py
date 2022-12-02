from math import *
def calculaExpressao(x):
    return x**2 - 5*x + 9

######## Dados para o metodo #########

constAurea = 0.618
N = 500
i = 1

xl = 0
xh = 4
E = 0.1

######################################

while i <= N:
    x1 = xh - constAurea * (xh - xl)
    x2 = xl + constAurea * (xh - xl)

    print("Iteração {}:\nx1 = {} e x2 = {}".format(i, x1, x2))
    print("xl = {} xh = {}".format(xl, xh))
    print("f(x1) = {} f(x2) = {}\n".format(calculaExpressao(x1), calculaExpressao(x2)))

    if calculaExpressao(x1) < calculaExpressao(x2):
        xh = x2
    else:
        xl = x1

    if abs(x2 - x1) < E:
        ponto = (x2 + x1) / 2
        print("\nFim das iteraçoes")
        print("Ponto: ", ponto)
        print("Numero de Iteraçoes: ", i)
        break

    i += 1

