# Algoritmos Generate-and-Test
Um CSP finito pode ser resolvido por um algoritmo exaustivo, também conhecido como brute force ou generate and test. O **espaço de atribuição**, *D*, é o conjunto de atribuições totais. O algoritmo retorna um modelo, ou todos os modelos.

O algoritmo **generate-and-test** para encontrar um modelo é o seguinte: 
1. Confere cada atribuição total uma a uma;
2. Se uma atribuição que satisfaz todas as restrições é encontrada, retorna a atribuição.

O algoritmo para retornar todos os modelos é parecido, mas ao invés de retornar o modelo, ele salva todos os modelos que satisfaz as restrições e então retorna todos os modelos.

Se cada uma dos *n* domínios das variaveis tem tamanho *d*, então *D* tem *d^n* elementos. Se existem *e* restrições, o número total de restrições testadas é *O(ed^n)*. De acordo com que *n* fica maior, o problema fica rapidamente intratável, então devemos encontrar soluções alternativas com menor tempo de execução.