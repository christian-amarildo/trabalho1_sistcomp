def decimal_para_binario(decimal):
    binario = '' # cria uma string vazia para armazenar o resultado em binário
    while decimal > 0: # enquanto o decimal for maior que zero
        resto = decimal % 2 # obtém o resto da divisão por 2
        binario = str(resto) + binario # concatena o resto ao início da string binário
        decimal //= 2 # divide o decimal por 2 e arredonda para baixo (divisão inteira)
    return binario # retorna a string com o número em binário

decimal = int(input("Coloque o número decimal para transformar em binário: ")) # recebe um número decimal do usuário e o converte para um inteiro
binario = "O decimal " + str(decimal) + " convertido para binário é " + decimal_para_binario(decimal) # chama a função decimal_para_binario para converter o número decimal em binário e cria uma string com a mensagem final
print(binario) # imprime a mensagem final na tela
