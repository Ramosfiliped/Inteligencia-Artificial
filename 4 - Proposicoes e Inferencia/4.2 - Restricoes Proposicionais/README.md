# Restrição Proposicionais
O [capítulo 3](../../3%20-%20Satisfa%C3%A7%C3%A3o%20de%20Restri%C3%A7%C3%A3o/) mostra como raciocinar como restrições. Fórmulas lógicas providenciam uma forma concisa de restrições com uma estrutura que pode ser explorada.

A classe de problemas de **satisfatibilidade proposicional** tem:
* Variáveis booleanas: Uma variável booleana é uma variável com domínio *{verdadeiro, falso}*. Se *X* é uma variável booleana, escrevemos *X = true* e sua forma equivalente em minúsculo, *x*, e escrevemos *X = false* como ¬*x*. Portanto, dado a variável booleana Feliz, a proposição *feliz* significa Feliz = true e ¬*feliz* significa Feliz = false
* Restrições de cláusula: Um **cláusula** é uma expressão na forma l1 v l2 v ... v lk onde cada *li* é um literal. Um **literal** é um átomo ou uma negação de um átomo, portanto um literal é uma atribuição de um valor a uma variável booleana. Uma clausula é satisfeita em um mundo possível se e somente se ao menos um dos literais que constituem uma clausula é verdadeiro nesse mundo possível.

Se ¬a aparecena na clausula, o átomo *a* é dito que aparece negativamente na clausula. Se *a* aparece não negado na cláusula, é dito que ele aparece positivamente na cláusula.