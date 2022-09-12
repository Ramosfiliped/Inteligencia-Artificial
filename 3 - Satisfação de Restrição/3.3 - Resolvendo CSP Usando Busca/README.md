# Resolvendo CSPs Usando Busca
Algoritmos generate-and-test atribui valores a todas as variáveis antes de checar as restrições. Porque restrições individuais envolvem apenas um subconjunto de vairáveis, algumas restrições podem ser testadas antes de todas as variáveis terem seu valor atribuído.
Se uma atribuição parcial é inconsistente com uma restrição, qualquer atribuição total que extende a atribuição parcial também será inconsistente.

Uma alternativa para algoritmos generate-and-test é construir um espaço de busca para a estratégia de busca utilizada no capítulo anterior.
O grafo de busca é definido a seguir:
* Os nós são atribuições de valores de algum subconjunto de variáveis.
* Os vizinhos de um nó *n* são obtidos selecionando uma variável *Y* que não está atribuída no nó *n* e tendo um vizinho para cada atribuição de um valor a *Y* que não viola nenhuma restrição.

Suponha que *n* é uma atribuição ***{X1 = v1, ..., Xk = vk}***. Para encontrar o vizinho de *n*, selecione uma variável *Y* que não está no conjunto ***{X1, ..., Xk}***. Para cada valor *yi* ∈ *dom(Y)*, onde *X1 = v1, ... Xk = vk*, *Y = yi* é consistente com cada restrição, o nó ***{X1 = v1, ..., Xk = vk}*** é vizinho de *n*.
* O nó inicial é a atribuição vazia que não atribui valor a nenhuma variável
* O nó objetivo é um nó que atribui valor a todas a variáveis. Note que ele só existe se a atribuição é consistente com todas as restrições.

Esse tipo de busca feito como busca em profundidade, é tipicamente chamado de **backtracking**, pode ser muito mais eficiênte do que o algoritmo generate-and-test.