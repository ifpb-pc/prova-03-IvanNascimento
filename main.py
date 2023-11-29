def q1(cidades: dict) -> list:
    resultado = []
    for cidade, idade in cidades.items():
        if idade > 100:
            resultado.append(cidade)
    return resultado


def q2(lista1: list, lista2: list) -> tuple:
    resultado = []
    soma = 0
    for elemento in lista1:
        if elemento > 0:
            soma += elemento
            resultado.append(elemento)
    for elemento in lista2:
        if elemento > 0:
            soma += elemento
            resultado.append(elemento)
    resultado.sort()
    return (soma, resultado)


def q3() -> tuple:
    return processa_lista(ler_valores())


def q4() -> list:
    valores = ler_03_alturas()
    resultado = []
    for i in valores:
        resultado.append(f"{i:.2f}")
    return resultado


def ler_valores():
    retorno = []
    while True:
        entrada = int(input())
        if entrada == 0:
            return retorno
        retorno.append(entrada)


def processa_lista(lista):
    pares = []
    impares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append(elemento)
        else:
            impares.append(elemento)
    return (pares, impares)


def ler_03_alturas():
    retorno = []
    for i in range(3):
        retorno.append(int(input()))
    return retorno


def organizar_alturas(valores):
    valores = valores.sort()
    return [valores[1], valores[2], valores[0]]


def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)

    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    soma, resultado = q2(lista1, lista2)
    print("q2:", soma, resultado)

    print("q3:", q3())

    print("q4:", q4())


if __name__ == "__main__":
    main()
