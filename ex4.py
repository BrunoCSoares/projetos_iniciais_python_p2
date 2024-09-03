# 4. Com a volta das aulas presenciais, a mãe de um aluno do ensino fundamental necessita saber quanto gastará com material escolar. Para fazer uma simulação, ela foi a uma livraria com o objetivo de simular a compra dos seguintes itens básicos: canetas, lápis e cadernos. Um ponto a se considerar é que essa livraria está com um programa de desconto de 20% nos preços dos cadernos e 5% nas canetas. Assim sendo, escreva um programa em Python que solicite as quantidades dos itens, preços e calcule o total da compra simulada.

qntCad = int(input("Informe a quantidade de cadernos comprados: "))
qntCan = int(input("Informe a quantidade de canetas compradas: "))
qntLap = int(input("Informe a quantidade de lápis comprados: "))
preCad = float(input("Informe o preço de cada caderno: "))
preCan = float(input("Informe o preço de cada caneta: "))
preLap = float(input("Informe o preço de cada lápis: "))

custoCad = qntCad * preCad * 0.8
custoCan = qntCan * preCan * 0.95
custoLap = qntLap * preLap
custo = custoCad + custoCan + custoLap

print(f"a compra csutará R${custo} sendo R${custoCad} de cadernos, R${custoCan} de canetas e R${custoLap} de lápis.")