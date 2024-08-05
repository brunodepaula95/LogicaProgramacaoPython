#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = input('Qual é o seu salário mensal:')
horas_trabalhadas_por_dia = input('Quantas horas trabalha por dia?')
dias_trabalhados_por_mes = input('Quantos dias por mês você trabalha?')

valor_hora = int (salario_mensal) / (int(dias_trabalhados_por_mes) * int(horas_trabalhadas_por_dia))


print(valor_hora)


#No exemplo dado pelo professor ele já coloca o total de horas trabalhadas no mês, mas em alguns casos se fosse um programa real, o usuário pode não saber como calcular o total de horas trabalhado por mês, dessa forma o programa fica mais acessível para estes usuários.