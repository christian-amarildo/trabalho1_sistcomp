def octal_para_binario(octal):
    # Dicionário para mapear cada dígito octal em um número binário de 3 bits
    dicionario = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
    # Converter cada dígito octal em um número binário de 3 bits e concatenar
    binario = ''.join([dicionario[digito] for digito in octal])
    return binario

def binario_para_octal(binario):
    # Adicionar zeros à esquerda para que o número de dígitos seja múltiplo de 3
    while len(binario) % 3 != 0:
        binario = '0' + binario
    # Dicionário para mapear cada grupo de 3 dígitos binários em um número octal
    dicionario = {'000':'0', '001': '1', '010': '2', '011': '3', '100':'4','101':'5','110':'6','111':'7'}
    octal= ''.join([dicionario[digito] for digito in [binario[i:i+3] for i in range(0, len(binario), 3)]])
    return octal


def hexa_para_binario(hexa):
    dicionario = {'0': '0000', '1': '0001', '2': '0010', '3': '0011','4': '0100', '5': '0101', '6': '0110', '7': '0111','8': '1000', '9': '1001', 'A': '1010', 'B': '1011','C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    binario = ''.join([dicionario[digito] for digito in hexa])
    return binario

def binario_para_hexa(binario):
    while len(binario) % 4 != 0:
        binario = '0' + binario
    dicionario = {'0000':'0' , '0001':'1' , '0010':'2' , '0011':'3' , '0100':'4' , '0101':'5' , '0110':'6' , '0111':'7' , '1000':'8' , '1001':'9','1010':'A','1011':'B','1100':'C','1101':'D','1110':'E','1111':'F'}
    hexa= ''.join([dicionario[digito] for digito in [binario[i:i+4] for i in range(0, len(binario), 4)]])
    return hexa

def binario_para_decimal (binario):
    decimal= 0
    potencia= len(binario)-1
    for digito in binario:
        decimal += int(digito)*2**potencia
        potencia -=1
    return decimal






octal=input("insira um número em octal para ser transformado em binario ")
print ("esse numero em binario é ", (octal_para_binario(octal)))
print ("esse numero octal que você colocou pode tambem ser representado em decimal como ", binario_para_decimal (octal_para_binario(octal)))


binario=input("insira um número em binario para ser tranformado em octal ")
print ("esse numero em octal é ", (binario_para_octal(binario)))

hexa=input("insira um número em hexa para ser transformado em binario ")
print ("esse numero em binario é ", (hexa_para_binario(hexa)))
print ("esse numero em hexadecimal que você colocou pode tambem ser representado em decimal como ", binario_para_decimal ((hexa_para_binario(hexa))))

binarioh=input("insira um número em binario para ser transformado em hexadecimal ")
print ("esse numero em hexadecimal é ", (binario_para_hexa(binarioh)))


