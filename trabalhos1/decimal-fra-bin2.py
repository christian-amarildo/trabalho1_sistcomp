
# Função para converter um número decimal fracionário em binário
def decimal_fracionario_para_binario(decimal):
    # Separa a parte inteira e fracionária do número decimal
    inteiro, fracionario = str(decimal).split(".")
    # Converte a parte inteira para binário
    binario_inteiro = bin(int(inteiro))[2:]

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

# Exemplo de uso
decimal_binario = input("Escreva o seu número decimal fracionário: ")
print("O seu número decimal fracionário convertido para binário é", decimal_fracionario_para_binario(decimal_binario))

binario_decimal = input("Escreva o seu número binário fracionário: ")
print("O seu número binário fracionário convertido para decimal é", binario_fracionario_para_decimal(binario_decimal))
















































# import math

# # Função para converter um número decimal fracionário em binário
# # Recebe como parâmetros o número decimal e o número de bits para a parte fracionária (16 bits por padrão)
# def decimal_fracionario_para_binario(decimal, num_bits=16):
#     # Separa a parte inteira e fracionária do número decimal
#     inteiro, fracionario = str(decimal).split(".")
#     # Converte a parte inteira para binário
#     inteiro_binario = decimal_para_binario(int(inteiro))
    
#     # Inicializa a parte fracionária em binário como uma string vazia
#     fracionario_binario = ""
#     # Converte a parte fracionária para float
#     fracionario = float("0." + fracionario)
    
#     # Enquanto a parte fracionária for maior que 0 e não ultrapassar o número de bits especificado
#     while fracionario > 0 and len(fracionario_binario) < num_bits:
#         # Multiplica a parte fracionária por 2
#         fracionario *= 2
#         # Se o resultado for maior ou igual a 1, adiciona 1 à parte fracionária em binário e subtrai 1 do resultado
#         if fracionario >= 1:
#             fracionario_binario += "1"
#             fracionario -= 1
#         # Caso contrário, adiciona 0 à parte fracionária em binário
#         else:
#             fracionario_binario += "0"
    
#     # Retorna o número inteiro e fracionário em binário concatenados com um ponto
#     return inteiro_binario + "." + fracionario_binario


# # Função para converter um número decimal inteiro em binário
# def decimal_para_binario(decimal):
#     # Se o número for 0, retorna "0" em binário
#     if decimal == 0:
#         return "0"
    
#     bits = []
#     # Enquanto o número for maior que 0
#     while decimal > 0:
#         # Calcula o resto da divisão por 2 e adiciona à lista de bits
#         resto = decimal % 2
#         bits.append(resto)
#         # Divide o número por 2
#         decimal //= 2
    
#     # Retorna a lista de bits convertida em uma string, com a ordem invertida
#     return "".join(str(bit) for bit in bits[::-1])


# # # Função para converter um número binário fracionário em decimal
# # def binario_fracionario_para_decimal(binario):
# #     # Separa a parte inteira e fracionária do número binário
# #     inteiro, fracionario = binario.split(".")
    
# #     # Converte a parte inteira em decimal
# #     decimal_inteiro = binario_para_decimal(inteiro)
    
# #     decimal_fracionario = 0
# #     # Para cada dígito da parte fracionária
# #     for i in range(len(fracionario)):
# #         # Se o dígito for 1, adiciona o valor correspondente à posição na soma dos valores fracionários
# #         if fracionario[i] == "1":
# #             decimal_fracionario += 2**(-(i+1))
    
# #     # Retorna a soma dos valores inteiro e fracionário em decimal
# #     return decimal_inteiro + decimal_fracionario


# # # Função para converter um número binário em decimal
# # def binario_para_decimal(binario):
# #     decimal = 0
# #     for i in range(len(binario)):
# #         if binario[i] == "1":
# #             decimal += 2**(len(binario)-i-1)
    
# #     return decimal
