# ep1-a-star

Grupo:

Juan Victor Suman, Lucas Gomes Santana, Matheus Eiji

**Lógica do Problema:**

Um labirinto é gerado através da quantidade de linhas e colunas dadas input do usuário que é, entao, preenchido com os terrenos dados (terra, água, areia, barreira). Após o mapa ser gerado (com posições 0,0 para início e M-1,N-1 para final), o caminho deve ser encontrado utilizando o algoritmo A* (A estrela) que, basicamente, busca o menor caminho possível entre dois pontos através do uso de **heurísticas** (custo de caminho do nó atual para o nó final), **g** (custo do caminho do nó inicial para o nó atual) e **f** (a soma de *h* e *g*) e a própria diferença do A* para outros algoritmos (como Dijkstra), é o calculo do caminho levando em consideração sempre o menor valor possível de f dos nós. Lembrando que, nesse problema, cada terreno tem um peso e, no caso da barreira, não é possível atravessar.

A implementação do A*, basicamente, utiliza duas listas.

Terrenos:

- Terra: 1
- Água: 3
- Areia: 6
- Barreira: X
- Posição final ou inicial: 0


**Explicação de como pensou o espaço de estados:**

É verificado a posição atual do nó, se ele esta no range do labirinto (mapa gerado), se o terreno atual é possível andar e, assim, vai criando as possibilidades de filhos e adicionando-os às listas verificando sempre no comeco do loop se ele já encontrou o caminho correto e, caso não encontre, retorna None.

**Heurística escolhida:**

A partir do valor h é possível definir diferentes tipos de heurísticas para calcular a distância. As duas utilizadas foram a Heurística Euclidiana (a distância em linha reta entre dois pontos usando o Teorema de Pitágoras) e a Heurística Manhattan (soma das diferenças absolutas de suas coordenadas). 

![1*RwxPrdfS0G0w68yAdw-6Cw](https://user-images.githubusercontent.com/37526699/165190512-73f9e67c-b446-4974-b36a-41b9d3f46e48.png)

![1*kYsOWlz9d7VFWEBYI8Cudg](https://user-images.githubusercontent.com/37526699/165190518-ec71a8c8-b29c-4a7c-bef4-e164c0c32713.png)


**Demonstração dos exemplos:**

Usando a Heurística Manhattan:

<img width="475" alt="Captura de Tela 2022-04-25 às 20 27 03" src="https://user-images.githubusercontent.com/37526699/165190619-0b2d79e3-0732-4b6e-93b8-34ac02f3a04d.png">

Usando a Heurística Euclidiana:

<img width="552" alt="Captura de Tela 2022-04-25 às 20 27 34" src="https://user-images.githubusercontent.com/37526699/165190666-0a5b105e-8669-490d-93d4-ba6b2c10a32d.png">
