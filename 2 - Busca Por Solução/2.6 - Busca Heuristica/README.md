# Busca Heurística

Os métodos de pesquisa das seções anteriores são **desinformados** (ou cegos) de maneira que não levam o objetivo em consideração antes de expandir os caminho até o nó que satisfaz o objetivo. Informações heurísticas sobre qual o nó mais promissor pode guiar a busca mudando qual o nó selecionado.

Uma **função heurística** *h(n)*, recebe um nó *n* e retorna um número real não negativo que é a estimativa do custo do caminho de menor custo a partir daquele nó *n* até o nó objetivo. A função *h(n)* é uma **heurística adimissível** se *h(n)* é sempre menor ou igual ao custo atual do caminho de menor custo a partir de um nó *n* até o nó objetivo.

Um simples uso da função heurística é na busca em profundidade para ordenar os vizinhos que são adicionados na pilha representando a fronteira. Os vizinhos podem ser adicionados na fronteira então o melhor vizinho é selecionado primeiro. Isso é conhecido como **busca em profundidade heurística**.

Outra maneira de utilizar a função heurística é sempre selecionar um caminho na fronteira com o menor custo de heurística. Isso é chamado **busca gulosa**. Este método as vezes funciona bem. Contudo, ele pode seguir caminhos que parecem promissores pois eles aparentam ser mais próximos do objetivo, mas o caminho explorado pode ir ficando maior.


## Busca A*
**Busca A*** usa tanto o custo do caminho, como em menor custo caminho primeiro, quanto a informação heurística, como na busca gulosa, para selecionar qual caminho expandir. Para cada caminho na fronteira, **A*** utiliza uma estimativa inicial do caminho total do nó inicial até o nó objetivo restrito a seguir esse caminho inicialmente. Ele usa o **custo(p)**, o custo do caminho encontrado, bem como a função heurística **h(p)**, uma estimativa do custo de *p* até o nó objetivo.

Para cada caminho *p* na fronteira, define ***f(p) = cost(p) + h(p)***. Isso é uma estimativa do custo total de seguir o caminho *p* e então ir para um nó objetivo.    

## Busca Branch-and-Bound
**Busca branch-and-bound** é uma maneira de combinar a otimização de espaço da busca em profundidade com a informação heurística para encontrar caminhos ótimos.
É particularmente aplicável quando existe vários caminhos para um objetivo. Assim como a busca **A***, a função heurística *h(n)* é não negativa e menor ou igual ao custo do caminho com menor custo de *n* até um nó objetivo.

A ideia do branch-and-bound é manter o caminho de menor custo até um objetivo encontrado até então, e seu custo. Suponha esse custo é o limite. Se a busca encontra um caminho *p* em que **cost(p) + h(p) >= limite**, *p* pode ser podado. Se um caminho não podado até um objetivo é encontrado, ele pode ser melhor que o antigo melhor caminho. Essa nova solução então é salva e o limite é atualizado para o custo da nova solução.