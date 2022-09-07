# Busca em Grafos
Neste capítulo, o problema de encontrar uma sequência de ações que alcançam um objetivo é abstraído como busca de um caminho em grafos. Para resolver o problema, primeiro definimos o espaço de busca subjacente e então aplicamos o algoritmo de busca de caminho em um grafo.

Um grafo direcionado consiste em um conjunto de nós e um conjunto de arcos direcionados entre os nós. A ideia é encontrar um caminho que saia do nó inicial e chegue ao nó final.

## Formalizando a busca em grafos

Um **grafo direcionado** consiste de 
* Um conjunto **N** de **nós**;
* Um conjunto **A** de arcos, onde um **arco** é uma ordenação do par de nós.

Nesta definição, um nó pode ser qualquer coisa. Pode ter infinitos nós e arcos. Não assumimos que um grafo é representado explicitamente, apenas requerimos um processo para gerar nós e arcos conforme o necessário.

O arco 
$$<n_1, n_2>$$
é um arco que sai do nó n1 e vai para n2.

O nó n2 é **vizinho** de n1 se existe um arco de n1 para n2.

Um **caminho** de um nó *s* para o nó *g* é a sequência de arcos <n0, n1, ..., nk> em que *s = n0, g = nk*, e que *<ni-1, ni>* está em **A**.

Um **objetivo** é uma função booleana em um nó. Se ***goal(s)*** é verdadeiro, dizemos que o nó *s* satisfaz o objetivo e portanto é um **nó objetivo**.