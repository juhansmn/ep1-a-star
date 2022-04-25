import random
from node import Node

#Terrenos:
#1: terra
#3: água
#6: área movediça
#X: intransponíveis
terrains = [0, 1, 3, 6, 'X']
walkable_terrains = [0, 1, 3, 6]
m, n = 0, 0
map = []

#cria o mapa inicial
def createRootMap():
  global map

  map = [[0 for col in range(n)] for row in range(m)]
    
#preenche o mapa com os terrenos
def fillMap():
  global map
  
  for i in range(0,m):
    for j in range(0,n):
      map[i][j] = random.choice(terrains)

  map[0][0] = 0
  map[m-1][n-1] = 0

#imprime um mapa
def printMap(map):
    for i in range(0,m):
        for j in range(0,n):
            print(f'[{map[i][j]:^5}]', end='')
        print()
    print('\n')

#implementação do algoritmo de a estrela que retorna uma lista de posições (tuplas)
def a_star_pathfind(map, start_point, end_point, is_euclidian):
    #cria nós da posição inicial e final
    start_node = Node(None, start_point)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end_point)
    end_node.g = end_node.h = end_node.f = 0

    #inicializa duas listas
    open_list = [] #possíveis caminhos
    closed_list = [] #o melhor caminho, os caminhos da lista aberta com menor f possível

    #adicionar o nó inicial na lista aberta
    open_list.append(start_node)

    #loop até você encontrar o final da lista aberta
    while len(open_list) > 0:

        # pega o nó atual (com menor f possível)
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # pop o indíce atual da lista aberta e adiciona à lista fechada
        open_list.pop(current_index)
        closed_list.append(current_node)

        # se encontrou o caminho correto
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # retorna o caminho feito

        #gera novos nós filhos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #nós adjacentes

            #pega a posição do nó
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #verifica se está no range
            if node_position[0] > (len(map) - 1) or node_position[0] < 0 or node_position[1] > (len(map[len(map)-1]) -1) or node_position[1] < 0:
                continue

            #verifica se o terreno a ser percorrido é possível andar
            if map[node_position[0]][node_position[1]] not in walkable_terrains:
                continue

            #cria um novo nó
            new_node = Node(current_node, node_position)

            #adiciona o novo nó aos filhos
            children.append(new_node)

        #loop nos nós filhos
        for child in children:

            #verifica se a criança está na lista fechada
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            #cria os valores f, g e h para o filho
            child.g = current_node.g + 1

            if is_euclidian:
                #Heuristica Euclidiana com aproximação do cálculo sem raíz quadrada
                child.h = calculate_euclidian_heuristics(child.position[0], end_node.position[0], child.position[1], end_node.position[1])
            else:
                #Heuristica Manhattan
                child.h = calculate_manhattan_heuristics(child.position[0], end_node.position[0], child.position[1], end_node.position[1])

            child.f = child.g + child.h

            #se o nó estiver na lista aberta
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #adiciona o filho na lista aberta
            open_list.append(child)

def calculate_euclidian_heuristics(first_x, first_y, second_x, second_y):
    return ((first_x - first_y) ** 2) + ((second_x - second_y) ** 2)

def calculate_manhattan_heuristics(first_x, first_y, second_x, second_y):
    return (abs(first_x - first_y) + abs(second_x - second_y))

def main():
  global m, n, map
  
  l, c = input("Digite o número de linhas e colunas (com espaço): ").split()
  m = int(l)
  n = int(c)

  print("Colunas: {} e Linhas: {}".format(m, n))
  print()

  is_euclidian = bool(input("Usar Heurística Euclidiana? (1 ou 0): "))

  createRootMap()
  fillMap()
  printMap(map)

  start_point = (0, 0)
  end_point = (m-1, n-1)
  
  path = a_star_pathfind(map, start_point, end_point, False)
  print(path)

if __name__ == '__main__':
    main()

