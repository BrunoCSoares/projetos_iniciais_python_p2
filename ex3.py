# 3. Desenvolva um algoritmo que calcule a distribuição da herança do Tio Patinhas.
# Tio Patinhas tem sua fortuna estimada em U$ 65.4 bilhões de dólares, sabendo que ele deixou um testamento para seus herdeiros:
#     - 15% para o orfanato dos Patinhos;
#     - 25% para seu sobrinho Pato Donald e;
#     - o restante dividido igualmente para seus sobrinhos-netos Huguinho, Zezinho e Luisinho, filhos de sua irmã mais nova Dumbela Pato, que os colocou sob os cuidados do tio e nunca mais os buscou.

heranca = 65.4
orfanato = heranca * 0.15
donald = heranca * 0.25
netos = heranca - orfanato -donald
cadaNeto = netos / 3

print(f"Tio Patinhas deixa como herança U${heranca}Bi distribuidos em U${orfanato}Bi para o orfanto dos patinhos U${donald}Bi para seu sobriho Pato Donald e U${netos}Bi para seus netos Huguinho, Zezinho e Luizinho, sendo U${cadaNeto}Bi para cada neto.")