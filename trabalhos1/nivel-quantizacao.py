import math

# Pede ao usuário o número de níveis de quantização
niveis = int(input("Digite o número de níveis de quantização: "))

# Calcula o número de bits necessários
bits = int(math.log2(niveis))

print("Número de bits necessários:", bits)

# Exibe todas as combinações dos bits
for i in range(niveis):
    binario = format(i,"0" + str(bits) + "b")
    print(i, ":", binario)