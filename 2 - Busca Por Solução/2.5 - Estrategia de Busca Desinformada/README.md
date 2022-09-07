# Estratégia de Busca Desinformada
Um problema determina um grafo, o nó inicial e o objetivo, mas não qual caminho selecionar na fronteira. Isto é trabalho para **estratégia de pesquisa**. Uma estratégia de pesquisa define a ordem em que os caminhos são selecionados para a fronteira.

Esta seção apresenta quatro estratégia de pesquisa desinformadas que não levam em conta a localização do objetivo.

## Busca em Largura
Na **busca em largura** a fronteira é implementada como **FIFO** (primeiro a entrar é o primeiro a sair), ou seja, uma **fila**. Portanto, o caminho selecionado na fronteira é o que foi adicionado primeiro.

Esta abordagem implica que o caminho a partir do nó inicial são gerados em ordem do número de arcos no caminho. 

Suponha que o fator de ramificação da busca é *b*. Se o próximo caminho a ser selecionado na fronteira contém *n* arcos, existe ao menos *b^(n-1)* elementos na fronteira. Todos esses caminhos contendo *n* ou *n+1* arcos. Portanto, a complexidade, tanto de espaço quanto de tempo, são exponenciais em números de arcos do caminho a um objetivo com menor número de arcos.

Este método garante, no entanto, encontrar uma solução, se existe, e irá encontrar uma solução com o menor número de arcos.

Busca em largura é útil quando
* O problema é pequeno o suficiente para o espaço não ser um problema
* Você quer uma solução com o menor número de arcos

É um método fraco quando todas soluções possuem muitos arcos ou existe uma heurística disponível.
Não é muito utilizado normalmente pelos grandes problemas onde grafos são gerados dinamicamente por causa da complexidade de espaço exponencial.

## Busca em Profundidade
Na **busca em profundidade**, a fronteira age como **LIFO** (Último a sair, primeiro a entrar), ou seja, uma **pilha**. Na pilha elementos são adicionados e removidos do topo da pilha.

Implementando a fronteira como uma pilha resulta em caminhos que são seguidos profundamente - pesquisando um caminho até o final antes de tentar um caminho alternativo.
Este método envolve um tipo de **backtracking**: o algoritmo seleciona a primeira alternativa em cada nó, e retrocede para a próxima alternativa quando percorreu todos os caminhos desde a primeira seleção. Alguns caminhos podem ser infinitos quando o grafo tem ciclos ou infinitos nós, em ambos os casos a pesquisa em profundidade pode nunca parar.

Na pesquisa em profundidade cada outro caminho na fronteira está na forma *<n0, ..., ni, m>*, para cada índice *i < k* e algum nó *m* que é um vizinho de *ni*, isto é, ele segue o caminho selecionado por vários arcos e então tem exatamente um nó extra.
Portando a froteira contém somente o caminho atual e caminhos para nós vizinhos do nó nesse caminho.
Se o fator de ramificação é *b* e o caminho selecinado na fronteira tem *k* arcos, pode existir no pior caso *k * (b-1)* outros caminhos na fronteira. 
Portanto, para busca em profundidade, o espaço usado em qualquer estágio é linear no número de arcos desde o início até o nó atual.

Se existe uma solução no primeiro ramo selecionado, a complexidade de tempo é linear em número de arcos no caminho. No pior caso, o algoritmo de profundidade pode ficar preso em ramificações infinitas e nunca encontrarem uma solução, mesmo se existir uma, para grafos infinitos ou grafos com ciclos. Se o grafo é uma árvore, com o fator de ramificação menor ou igual a *b* e todos os caminhos desde o inicio tem *k* ou menos arcos, o pior caso tem complexidade de tempo *O(b^k)*.

Pesquisa em profundidade é apropriada quando
* O espaço é estrito
* Existem várias soluções, talvez com caminhos longos, principalmente para o caso em que quase todos os caminhos levam a uma solução
* A ordem em que os vizinhos de um nó são adicionados na pilha podem ser ajustado para que as soluções sejam encontradas na primeira tentativa.

E é um método ruim quando
* É possível ser pego em caminhos infinitos, que ocorrem em grafos infinitos ou grafos com ciclos
* soluções existem em profundidade rasa, porque neste caso a busca pode explorar muitos caminhos longos antes de encontrar as soluções curtas
* Existem muitos caminhos para um nó


## Busca Iterativa em Profundidade
Nenhum dos métodos anteriores é ideal. A pesquisa em largura, a qual garante que um caminho será encontrado, requere um espaço exponencial.
A pesquisa em profundidade pode não funcionar em grafos infinitos ou grafos com ciclos. Uma maneira de combinar a eficiência de espaço da busca em profundidade com a optimalidade da busca em largura é utilizar o **aprofundamento iterativo**.

Busca iterativa em profundidade chama repetidamente um buscador de pesquisa em profundidade, um pesquisador de profundidade que recebe um limite de profundidade inteiro e nunca explora caminhos com mais arcos do que esse limite de profundidade.


## Busca com Menor Custo
Para vários domínios, arcos tem um custo, e o objetivo é encontrar uma **solução ótima**, uma solução que tenha o menor custo possível.

O método de pesquisa mais simples que garante encontrar um caminho de custo mínimo é a **busca com menor custo primeiro**, que é similar a busca em largura, mas ao invés de expandir um caminho com menor número de arcos, ele seleciona o caminho com menor custo. Isto é implementado tratando a fronteira como uma fila de prioridade ordenada pela função de custo.