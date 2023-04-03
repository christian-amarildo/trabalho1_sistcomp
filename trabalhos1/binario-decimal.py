def binario_para_decimal (binario):
    decimal= 0
    potencia= len(binario)-1
    for digito in binario:
        decimal += int(digito)*2**potencia
        potencia -=1
    return decimal

binario= input("coloque o numero binario para tranformar em decimal ")
decimal = "O binário " + binario + " convertido para decimal é " + str(binario_para_decimal(binario))
print (decimal)