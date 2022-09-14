# Exercícios
1. Quais são os componentes de um problema de satisfação de restrições?

**R:**

* Variáveis: Parte do problema que será manipulado em busca de uma solução
* Domínio: Possíveis valores para as variáveis
* Restrições: Regras de valores para as variáveis, essas regras podem ser entre duas variáveis diferentes (A < B), ou menos entre somente uma variável e um valor (A > 4)

2. Explique o funcionamento do algoritmo generate-and-test.
   
**R:** Esse algoritmo gera todas as possibilidades de valores possíveis e confere uma a uma se há uma violação de restrição, caso não esse valor é retornado.

3. Como podemos utilizar algoritmos de busca do capítulo anterior para resolver CSPs?
   
**R:** Podemos tratar cada possibilidade de atribuição (total ou parcial) como se fose um nó. Se a diferença entre dois nós é de somente uma atribuição, então estes são nós vizinhos. 

Com isso temos um grafo e podemos aplicar por algoritmos de busca, onde os nós objetivos são aqueles nós cujo todas as variáveis tem algum valor atribuído e nenhuma restrição é violada para esse conjunto de atribuições.

4. Considere o seguinte CSP:
   
   X = {A, B, C}
   D = {{1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}}
   C = {A < B, B < C}

a. Qual o tamanho do espaço de busca? Ou seja, no pior caso, quantas soluções candidatas podem ser geradas?

**R:** Como o algoritmo generate-and-test testa todas as possibilidade completas possíveis, basicamente temos um problema de contagem. 

Como todas as variáveis tem um domínio de tamanho 4, temos 4³ possibilidades. Portanto 64 possibilidades no pior caso.

b. Represente esse problema como uma rede de restrições.

**R:**
![Árvore de Restrição](Arvore%20de%20Restricao.jpg)

5. Implemente o problema das [N-Rainhas](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
**R:** [Solução](./../Implementacao/nQueensBackTracking.py)