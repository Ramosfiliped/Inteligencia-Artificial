# Mundo Possível, Variáveis e Restrições
## Variaveis e Mundos
Problemas de satisfação de restrições são descritos em termos de variáveis e mundos possíveis. Um **mundo possível** é uma maneira possível de o mundo (o mundo real ou algum mundo imaginário) ser. 

Mundos possíveis são descritos por variáveis algébricas. Uma **variável algébrica** é um símbolo usado para denotar características do mundo possível. Para esse capítulo, nos referimos a uma variável algébrica simplesmente como **variável**. Variáveis algébricas são escritas começando com uma letra maiúscula. Cada variável algébrica **X** tem um **domínio** associado, ***dom(X)***, o qual é um conjunto de valores que uma variável pode ter.

Dado um conjunto de variáveis, uma **atribuição** na conjunto de variáveis é uma função das variáveis no domínio das variáveis. Nós escrevemos uma atribuição em **{X1, X2, ..., Xk}** como **{X1 = v1, X2 = v2, ..., Xk = vk}**, onde vi está no ***dom(Xi)***. Uma **atribuição total** atribui valores para todas as variáveis.

Um **mundo possível** é definido para ser uma atribuição total.

## Restrições
Em vários domínios, nem todas as atribuições de valores são permissíveis às variáveis. Uma **restrição rígida**, ou simplesmente **restrição**, especifica combinações legais de atribuições de valores a algumas das variáveis.

Um **escopo** é um conjunto de variáveis. Uma **relação** no escopo *S* é uma função de atribuições em *S* para **{true, false}**. Ou seja, 