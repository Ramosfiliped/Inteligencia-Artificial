# Um Algoritmo de Busca Genérico
Esta seção descreve um algoritmo de busca genérico para busca de caminho solução em grafos. O algoritmo chama procedimentos que podem ser implementadas em várias estratégias de busca.

A ideia intuitiva por trás do algoritmo de busca genérico, dado um grafo, um nó inicial, e um objetivo, é explorar caminhos incrementalmente do nó inicial. Isto é feito mantendo uma **fronteira** de caminhos do nó inicial até o nó objetivo.

Inicialmente, a fronteira contém o caminho trivial que contendo somente o nó inicial, e nenhum arco. De acordo com o proseguimento da busca, a fronteira se expande em nós não explorados até um nó objetivo ser encontrado.
Diferentes estratégias de busca são obtidas providenciando uma implementação apropriada da fronteira.

```
função Search(G, s, goal)
    Entradas
        G: Grafo com nós N e arcos A
        s: Nó inicial
        goal: Funções booleanas dos nós
    
    Saída
        Caminho de s até um nó para qual a função goal é verdadeira, ou retorna vazio caso não haja solução
    
    Variaveis
        fronteira: conjunto de caminhos
        fronteira := {<s>}
        enquanto fronteira != {} faca
            selecione e remova <n0, ..., nk> da fronteira
            se goal(nk) então
                return <n0, ..., nk>
            fronteira := fronteira + {<n0, ..., nk, n> : <nk, n>}
        return null
```

O **algoritmo de busca genérico** é mostrado acima. A fronteira é um conjunto de caminho. Inicialmente ela tem o caminho de custo zero com apenas o nó inicial. Se *goal(s)* é verdadeiro, então uma solução foi encontrada e retorna o caminho <n0, ..., nk>. Senão, o caminho é extendido em mais um arco encontrando os vizinhos de *nk*. Para cada vizinho de *n* de *nk*, o caminho *<n0, ..., nk, n>* é adicionado na fronteira. Esse passo é conhecido como **expansão** do caminho *<n0, ..., nk>*.