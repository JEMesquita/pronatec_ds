# Lista para armazenar os itens
itens = ["Espada", "Escudo", "Poção", ]

#//TODO: Solicite os itens ao usuário

for i in range(1, 4):
  item = input(f"Informe o nome do item {i}: ")
  itens.append(item)
  print("Lista de itens: ")
for item in itens:
  print(f"-{item}")