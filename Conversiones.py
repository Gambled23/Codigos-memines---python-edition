import numbers

# Convertir de numero a cadena
num = str(5.3)
# Convertir de decimal a binario
numBin = bin(6)
# Convertir de decimal a hexadecimal
numHex = hex(32)
# Convertir de binario a decimal
numBinDec = int(0b1100)  # el 0b indica que es binario
# Redondear
numRed = round(5.7)
# Longitud de una cadena
cadena1 = len("Pablo")

print(num)
print(numBin)
print(numHex)
print(numBinDec)
print(numRed)
print("La cadena Pablo tiene ", cadena1, "Caracteres")
