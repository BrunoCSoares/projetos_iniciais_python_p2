# 2. Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

totEle = int(input("Informe o número total de eleitores: "))
votBran = int(input("Informe o número de votos brancos: "))
votNul = int(input("Informe o número de votos nulos: "))
votVal = int(input("Informe o número de votos válidos: "))

perBran = 100/totEle*votBran
perNul = 100/totEle*votNul
perVal = 100/totEle*votVal

print(f"na cidade com {totEle} de votos {perBran:.0f}% são votos brancos, {perNul:.0f}% são votos nulos e {perVal:.0f}% são válidos.")