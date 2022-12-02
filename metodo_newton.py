from sympy import *

x = Symbol("x")
i = 1
N = 500


def calculaDerivadaPrimeira(function, x, valorx):
    derivadaPrimerira = parse_expr(str(diff(function, x)))
    derivadaPrimerira = derivadaPrimerira.evalf(subs={x: valorx})
    return derivadaPrimerira


def calculaDerivadaSegunda(function, x, valorx):
    derivadaSegunda = parse_expr(str(diff(function, x, 2)))
    derivadaSegunda = derivadaSegunda.evalf(subs={x: valorx})
    return derivadaSegunda


######## Dados para o metodo #########

function = x**3 - 5 * log(x) + 6
pontoAnterior = 1
ponto = 0
erro = 0.1

######################################


while i <= N:
    ponto = pontoAnterior - (
        calculaDerivadaPrimeira(function, x, pontoAnterior)
        / calculaDerivadaSegunda(function, x, pontoAnterior)
    )

    print("\nIteracao: ", i)
    print("ponto: ", ponto)

    if abs(ponto - pontoAnterior) < erro:
        print("\nFim das iteraçoes")
        print("Ponto: ", ponto)
        print("Numero de Iteraçoes: ", i)
        break

    pontoAnterior = ponto

    i += 1
