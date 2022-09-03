# Resolvendo Problemas Como Busca
No caso simples de um agente decidindo o que fazer, o agente tem um modelo baseado em estados do mundo, com o objetivo a ser alcançado incerto.
Isto é uma representação horizontal (não hierárquico) ou um único nível de hierarquia.
O agente é capaz de determinar como alcançar seus objetivos buscando em sua representação de espaços de estados do mundo, por uma maneira de sair do estado atual para o estado que satisfaça o objetivo. Dado um modelo completo, ele tenta encontra a sequência de ações que alcançam o objetivo antes de agir no mundo.

Este problema pode ser abstraído para o problema matemático de encontrar um caminho a partir de um nó inicial até um nó objetivo em um grafo direcionado. Vários outros problemas podem ser mapeados para essa abstração, então vale a pena considerar este nível de abstração.

A busca está por trás de grande parte da inteligência artificial. Quando um agente recebe um problema, é dado normalmente a descrição para reconhecer a solução, não o algoritmo para resolvê-lo. Ele tem que buscar pela solução. A existência dos problemas NP-Completo, com meios eficientes para reconhecer soluções, mas sem métodos eficientes para encontrá-las, indica que a busca é uma parte necessária da solução de problemas.