from math import pi
from statistics import mean
from os import system


# Funções auxiliares

# Função de validação de número
def checklist(msg=''):
    while True:
        next_number = input(msg)
        # Remover ponto para testar se a string possui apenas números
        test = next_number.replace('.', '', 1)
        # Caso o valor informado não seja numérico, passar pela função retry
        # testar se o primeiro caracter é indicativo de número positivo ou negativo,
        # para a validação só considerar a parte númerica
        # Teste caso a string esteja vazia
        if test:
            if test[0] in '+-':
                if not test[1:].isnumeric():
                    print('ERRO: Valor informado não é um número.')
                    main_menu = retry()
                    if main_menu == 'continue':
                        return 'continue'
                else:
                    return float(next_number)
            elif not test.isnumeric():
                print('ERRO: Valor informado não é um número.')
                main_menu = retry()
                if main_menu == 'continue':
                    return 'continue'
            # Caso seja outra operação genérica,
            # a única validação é se o valor informado é mesmo um número
            else:
                return float(next_number)
        else:
            print('ERRO: Valor informado não é um número.')
            main_menu = retry()
            if main_menu == 'continue':
                return 'continue'


# Função para decidir se após erro, o programa irá voltar ao menu principal
def retry():
    while True:
        answer = input('Deseja voltar ao menu principal? (S/N)\n').strip().upper()
        if answer == 'S' or answer == 'N':
            if answer == 'S':
                return 'continue'
            break
        print('ERRO: Opção inválida')


# Função para decidir se serão informados mais números,
# ou apresentar o resultado
def finish():
    while True:
        answer = input('Deseja continuar? (S/N)\n').strip().upper()
        if answer in 'S_N':
            return answer
        print('ERRO: Opção inválida!')


# Função para decorar a seleção
def selection(msg):
    msg_size = len(msg) + 10
    print('-' * msg_size)
    print(f'{msg:^{msg_size}}')
    print('-' * msg_size)


# --------------------------------------------------------


# Operações matemáticas

# Função soma
def soma():
    while True:
        # Pedir os números a serem somados
        next_val = checklist('Digite um número: ')
        if next_val == 'continue':
            break
        else:
            # Adicionar o número a ser somado na lista
            numbers.append(next_val)
            end = finish()
            if end == 'N':
                break
    if next_val == 'continue':
        return 'continue'
    # Somar e apresentar resultado
    return numbers, sum(numbers)

# Função subtração
def subtracao():
    while True:
        # Pedir números a serem subtraídos
        next_val = checklist('Digite um número: ')
        if next_val == 'continue':
            break
        else:
            # Adicionar números na lista
            numbers.append(next_val)
            end = finish()
            if end == 'N':
                break
    if next_val == 'continue':
        return 'continue'
    # Subtrair números e apresentar resultado
    for idx, val in enumerate(numbers):
        # Caso seja o primeiro número da lista, considerar como número base
        if idx == 0:
            result = val
        else:
            result -= val
    return numbers, result


# Função multiplicação
def multiplicacao():
    while True:
        # Pedir números a serem multiplicados
        next_val = checklist('Digite um número: ')
        if next_val == 'continue':
            break
        else:
            # Adicionar números na lista
            numbers.append(next_val)
            end = finish()
            if end == 'N':
                break
    if next_val == 'continue':
        return 'continue'
    # Calcular e apresentar resultado
    if 0 not in numbers:
        for idx, val in enumerate(numbers):
            # Caso seja o primeiro número da lista, considerar como número base
            if idx == 0:
                result = val
            else:
                result *= val
        return numbers, result
    else:
        return numbers, 0


# função divisão
def divisao():
    pass


# função potência
def potencia():
    pass


# função raiz quadrada
def raiz_quadrada():
    pass


# função média
def media():
    pass


# função máximo
def maximo():
    pass


# função mínimo
def minimo():
    pass


# Função para calcular a área escolhida pelo usuário
def area(shape):
    # ÁREA DO QUADRADO / RETÂNGULO
    if shape == 1:
        selection('RETÂNGULO/QUADRADO SELECIONADO')
        while True:
            base = checklist('Digite o tamanho da base: ')
            if base <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                base = retry()
                if base == 'continue':
                    return 'continue'
            else:
                break
        while True:
            height = checklist('Digite o tamanho da altura: ')
            if height <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                height = retry()
                if height == 'continue':
                    return 'continue'
            else:
                break
        result = base * height
    # ÁREA DO TRAPÉZIO
    elif shape == 2:
        selection('TRAPÉZIO SELECIONADO')
        while True:
            lower_base = checklist('Digite o tamanho da base menor: ')
            if lower_base <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                lower_base = retry()
                if lower_base == 'continue':
                    return 'continue'
            else:
                break
        while True:
            higher_base = checklist('Digite o tamanho da base maior: ')
            if higher_base <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                higher_base = retry()
                if higher_base == 'continue':
                    return 'continue'
            else:
                break
        while True:
            height = checklist('Digite o tamanho da altura: ')
            if height <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                height = retry()
                if height == 'continue':
                    return 'continue'
            else:
                break
        result = ((higher_base + lower_base) * height) / 2
    # ÁREA DO TRIÂNGULO
    elif shape == 3:
        selection('TRIÂNGULO SELECIONADO')
        while True:
            base = checklist('Digite o tamanho da base: ')
            if base <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                base = retry()
                if base == 'continue':
                    return 'continue'
            else:
                break
        while True:
            height = checklist('Digite o tamanho da altura: ')
            if height <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                height = retry()
                if height == 'continue':
                    return 'continue'
            else:
                break
        result = (base * height) / 2
    # ÁREA DA CIRCUNFERÊNCIA
    else:
        selection('CIRCUNFERÊNCIA SELECIONADA')
        while True:
            radius = checklist('Digite o tamanho do raio: ')
            if radius <= 0:
                print('ERRO: Valor informado não pode ser menor ou igual a 0!')
                radius = retry()
                if radius == 'continue':
                    return 'continue'
            else:
                break
        result = pi * (radius ** 2)
    # Retornar o valor da área calculada
    return float(result)


# função perímetro
def perimetro():
    pass


if __name__ == '__main__':
    # Criar o menu
    option = ''
    numbers = []
    while True:
        # Limpar o menu, limpar a lista de números para operações
        numbers.clear()
        system('cls')
        # Imprimir menu
        print('-' * 20)
        print('Escolha uma opção:')
        print('A - Somar\n'
            'B - Subtrair\n'
            'C - Multiplicar\n'
            'D - Dividir\n'
            'E - Potência\n'
            'F - Raiz Quadrada\n'
            'G - Média\n'
            'H - Máximo\n'
            'I - Mínimo\n'
            'J - Área\n'
            'K - Perímetro\n'
            'S - Sair')
        print('-' * 20)
        # receber opçao do usuário
        option = input().upper().strip()

        # Calculadora fecha caso opção seja SAIR
        if option == 'S':
            break

        # SOMA
        elif option == 'A':
            system('cls')
            selection('SOMA SELECIONADA')
            resultado = soma()
            if resultado == 'continue':
                continue
            else:
                print(*resultado[0], sep=' + ', end=' = ')
                print(resultado[1])
                input()

        # SUBTRAIR
        elif option == 'B':
            system('cls')
            selection('SUBTRAÇÃO SELECIONADA')
            resultado = subtracao()
            if resultado == 'continue':
                continue
            else:
                print(*resultado[0], sep=' - ', end=' = ')
                print(resultado[1])
                input()
            
        # MULTIPLICAR
        elif option == 'C':
            system('cls')
            selection('MULTIPLICAÇÃO SELECIONADA')
            resultado = multiplicacao()
            if resultado == 'continue':
                continue
            else:
                print(*resultado[0], sep=' * ', end=' = ')
                print(resultado[1])
                input()

        # DIVIDIR
        elif option == 'D':
            system('cls')
            selection('DIVISÃO SELECIONADA')
            while True:
                # Pedir números a serem divididos
                next_val = checklist('Digite um número: ')
                if next_val == 'continue':
                    break
                # Caso algum dividendo seja igual a zero, apresentar erro
                elif next_val == 0 and len(numbers) != 0:
                    print('ERRO: Impossível dividir por ZERO!')
                    next_val = retry()
                    if next_val == 'continue':
                        break
                # Adicionar números na lista
                else:
                    numbers.append(next_val)
                    end = finish()
                    if end == 'N':
                        break
            if next_val == 'continue':
                continue
            # Calcular e apresentar resultado
            for idx, val in enumerate(numbers):
                # Caso seja o primeiro número da lista, considerar como número base
                if idx == 0:
                    result = val
                else:
                    result /= val
            print(*numbers, sep=' / ', end=' = ')
            print(result)
            input()

        # POTÊNCIA
        elif option == 'E':
            system('cls')
            selection('POTÊNCIA SELECIONADA')
            # Pedir número que será elevada para a n-potência
            while True:
                number = checklist('Digite um número: ')
                if number == 'continue':
                    break
                # Pedir potência
                power = checklist('Digite seu expoente: ')
                if power == 'continue':
                    break
                # Evitar que o programa tente calcular raiz par de número negativo
                elif power != 0:
                    if (1 / power) % 2 == 0 and number < 0:
                        print('ERRO: Raiz par de número negativo.')
                        power = retry()
                        if power == 'continue':
                            break
                    else:
                        break
                else:
                    break
            if number == 'continue' or power == 'continue':
                continue
            # Calcular e apresentar resultado
            result = number ** power
            print(f'{number} ^ {power} = {result}')
            input()

        # RAIZ QUADRADA
        elif option == 'F':
            system('cls')
            selection('RAIZ QUADRADA SELECIONADA')
            # Pedir número para se tirar raiz quadrada
            while True:
                number = checklist('Digite um número: ')
                if number == 'continue':
                    break
                elif number < 0:
                    print('ERRO: número informado não pode ser menor que ZERO!')
                    number = retry()
                    if number == 'continue':
                        break
                else:
                    break
            if number == 'continue':
                continue
            # Calcular e apresentar resultado
            result = number ** 0.5
            print(f'sqrt({number}) = {result}')
            input()
            
        # MÉDIA
        elif option == 'G':
            system('cls')
            selection('MÉDIA SELECIONADA')
            while True:
                # Pedir números que serão tirados a média
                next_val = checklist('Digite um número: ')
                if next_val == 'continue':
                    break
                # Adicionar números na lista
                else:
                    numbers.append(next_val)
                    end = finish()
                    if end == 'N':
                        break
            if next_val == 'continue':
                continue
            # Calcular e apresentar resultado
            result = mean(numbers)
            print(f'Média de {numbers} = {result}')
            input()
        
        # MÁXIMO
        elif option == 'H':
            system('cls')
            selection('MÁXIMO SELECIONADO')
            while True:
                # Pedir números aos quais será apresentado o maior deles
                next_val = checklist('Digite um número: ')
                if next_val == 'continue':
                    break
                # Adicionar números na lista
                else:
                    numbers.append(next_val)
                    end = finish()
                    if end == 'N':
                        break
            if next_val == 'continue':
                continue
            # Apresentar qual é o maior número da lista apresentada
            result = max(numbers)
            print(f'Máximo de {numbers} = {result}')
            input()
            
        # MÍNIMO
        elif option == 'I':
            system('cls')
            selection('MÍNIMO SELECIONADO')
            while True:
                # Pedir números aos quais será apresentado o menor deles
                next_val = checklist('Digite um número: ')
                if next_val == 'continue':
                    break
                # Adicionar números na lista
                else:
                    numbers.append(next_val)
                    end = finish()
                    if end == 'N':
                        break
            if next_val == 'continue':
                continue
            # Apresentar qual é o menor número da lista apresentada
            result = min(numbers)
            print(f'Mínimo de {numbers} = {result}')
            input()

        # ÁREA
        elif option == 'J':
            system('cls')
            while True:
                selection('ÁREA SELECIONADA')
                # Perguntar qual é a forma geométrica para o cálculo da área
                print('Escolha uma forma geométrica para calcular a área')
                print('-' * 20)
                print('1 - Quadrados e Retângulos\n'
                    '2 - Trapézios\n'
                    '3 - Triângulos\n'
                    '4 - Circunferências')
                print('-' * 20)
                decision = checklist()
                if decision == 'continue':
                    break
                # Indicar erro caso seja feita uma opção inválida
                elif decision in range(1, 5):
                    break
                else:
                    print('ERRO: Opção inválida!')
                    decision = retry()
                    if decision == 'continue':
                        break
            if decision == 'continue':
                continue
            # Usar função area() para calcular a área desejada
            else:
                result = area(int(decision))
                if result == 'continue':
                    continue
            # Apresentar resultado
            print(f'Área = {result:.2f}')
            input()
            
        # PERÍMETRO
        elif option == 'K':
            system('cls')
            selection('PERÍMETRO SELECIONADO')
            # Pedir o número de lados do perímetro que será calculado
            while True:
                sides = checklist('Digite o número de lados da sua forma geométrica'
                                ' (0 caso seja circunferência): ')
                if sides < 0 or not sides.is_integer() or 0 < sides <= 2:
                    print('ERRO: Número inválido de lados.')
                    sides = retry()
                    if sides == 'continue':
                        break
                else:
                    break
            # Caso seja escolhida uma circunferência, pedir o valor do raio e fazer
            # o cálculo
            if sides == 0:
                while True:
                    radius = checklist('Digite o raio da circunferência: ')
                    if radius <= 0:
                        print('ERRO: Valor inválido para tamanho de raio.')
                        radius = retry()
                        if radius == 'continue':
                            break
                    else:
                        break
                if radius == 'continue':
                    continue
                result = 2 * pi * radius
            # Caso contrário, pedir o tamanho de cada lado da forma geométrica
            # pedida e calcular o perímetro
            elif sides != 'continue':
                for i in range(int(sides)):
                    while True:
                        next_val = checklist(f'Digite o tamanho do {i + 1}° lado: ')
                        if next_val == 'continue':
                            break
                        elif next_val > 0:
                            break
                        elif next_val <= 0:
                            print('ERRO: Valor inválido para tamanho de lado.')
                            next_val = retry()
                            if next_val == 'continue':
                                break
                    if next_val == 'continue':
                        break
                    else:
                        numbers.append(next_val)
                if next_val == 'continue':
                    continue
                result = sum(numbers)
            else:
                continue
            # Apresentar resultado
            print(f'Perímetro = {result}')
            input()
            
        else:
            # Caso seja selecionada uma opção inválida,
            # o programa irá indicar o erro e reimprimir o menu
            print('ERRO: Opção inválida!')
            input()
