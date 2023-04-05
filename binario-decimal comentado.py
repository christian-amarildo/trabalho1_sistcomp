# Define a função para converter um número binário para decimal
def binario_para_decimal(binario):
    # Inicializa as variáveis para o cálculo do decimal
    decimal = 0
    potencia = len(binario) - 1 # Define a potência inicial, que é o número de dígitos do binário - 1
    
    # Itera pelos dígitos do binário, calculando o decimal a cada iteração
    for digito in binario:
        decimal += int(digito) * 2 ** potencia # Calcula o decimal correspondente ao dígito e adiciona à variável decimal
        potencia -= 1 # Decrementa a potência para o próximo dígito
    
    # Retorna o valor decimal calculado
    return decimal

# Solicita que o usuário informe um número binário a ser convertido
binario = input("Digite um número binário para converter para decimal: ")

# Chama a função binario_para_decimal e exibe o resultado na tela
decimal = "O binário " + binario + " convertido para decimal é " + str(binario_para_decimal(binario))
print(decimal)
