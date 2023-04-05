# Função para converter um número decimal fracionário em binário
def decimal_fracionario_para_binario(decimal):
    # Separa a parte inteira e fracionária do número decimal
    inteiro, fracionario = str(decimal).split(".")
    
    # Converte a parte inteira para binário
    def decimal_inteiro_para_binario(decimal):
        binario = ''
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal //= 2
        return binario
    
    binario_inteiro = decimal_inteiro_para_binario(int(inteiro))
    
    # Converte a parte fracionária para binário
    decimal_fracionario = float("0." + fracionario)
    binario_fracionario = ""
    while decimal_fracionario > 0:
        decimal_fracionario *= 2
        if decimal_fracionario >= 1:
            binario_fracionario += "1"
            decimal_fracionario -= 1
        else:
            binario_fracionario += "0"

    # Retorna o número binário completo
    if binario_fracionario:
        return binario_inteiro + "." + binario_fracionario
    else:
        return binario_inteiro

# Função para converter um número binário fracionário em decimal
def binario_fracionario_para_decimal(binario):
    # Separa a parte inteira e fracionária do número binário
    inteiro, fracionario = binario.split(".")
    
    # Converte a parte inteira para decimal
    decimal_inteiro = int(inteiro, 2)
    
    # Converte a parte fracionária para decimal
    decimal_fracionario = 0
    for i, digito in enumerate(fracionario):
        decimal_fracionario += int(digito) * 2 ** -(i + 1)

    return decimal_inteiro + decimal_fracionario


#saida
decimal_binario = input("Escreva o seu número decimal fracionário: ")
print("O seu número decimal fracionário convertido para binário é", decimal_fracionario_para_binario(decimal_binario))

binario_decimal = input("Escreva o seu número binário fracionário: ")
print("O seu número binário fracionário convertido para decimal é", binario_fracionario_para_decimal(binario_decimal))

#Comentário:
#Esse código contém duas funções que convertem números decimais fracionários em binário e binário fracionário em decimal,
# respectivamente. A primeira função "decimal_fracionario_para_binario" recebe um número decimal fracionário como entrada e retorna
#sua representação em binário como uma string. A segunda função "binario_fracionario_para_decimal" recebe um número binário fracionário
#como entrada e retorna seu valor em decimal como um número. Ambas as funções funcionam dividindo o número em suas partes inteiras
#e fracionárias, convertendo cada uma separadamente e, em seguida, juntando as duas partes para obter o número completo.
