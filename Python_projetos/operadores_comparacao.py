# operadores ---> operacções
# == Igual a 
# != Diferente de 
# > maior que
# < Menor que
# >= Maior ou igual a 
# <= Menor ou igual a 

x = y = z = False
n1 = n2 = 0

print("Digite um número:")
n1 = int(input())
n2 = int (input("Digite outro número:"))

x = n1 == n2
print("São Iguais?", x, '\n')

z = n1> n2
print(n1, 'é maior que', n2, '?', z, '\n')

y = n1 != n2
print('São difernete?' +str(y))