# funções
def mostrar_menu():
    print('1 - Calcular quadrilátero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Sair do programa.')

def calcular_quadrilatero(b, h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14*(r**2)
    return result

# programa principal
while True:
    mostrar_menu()

    opcao = input('Opção desejada: ')

    match opcao:
        case '1':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do quadrilatero: {calcular_quadrilatero(b, h)}.')
            continue
        case '2':
            b = float(input('Informe o valor da base: ').replace(',', '.'))
            h = float(input('Informe o valor da altura: ').replace(',', '.'))
            print(f'Área do triangulo: {calcular_triangulo(b, h)}.')
            continue
        case '3':
            r = float(input('Informe o valor da base: ').replace(',', '.'))
            print(f'Área do circulo: {calcular_circulo(r)}.')
            continue 
        case '4':
            print('Porgrama encerrado.')
            break
        case _:
            print('Opção invalida.')