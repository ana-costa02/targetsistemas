#verificação de pertencimento na sequência Fibonacci
def pertence_sequencia_fibonacci(numero):
    # Casos base
    if numero == 0 or numero == 1:
        return True
    
    # Inicializando os dois primeiros números da sequência
    a, b = 0, 1

    # Gerando os números da sequência até ultrapassar o número fornecido
    while b <= numero:
        # Verifica se o número fornecido está na sequência
        if b == numero:
            return True
        # Atualiza os valores para o próximo número na sequência
        a, b = b, a + b

    # Se o número não foi encontrado na sequência até agora
    return False

# Teste
numero = int(input("Informe um número: "))
if pertence_sequencia_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
