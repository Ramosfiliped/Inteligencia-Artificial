# Exercícios
1. Considere a seguinte base de conhecimento (KB):
   a <- b ^ c

   b <- c
   
   b <- d
   
   c
   
   d <- h
   
   e
   
   g <- a ^ b ^ c
   
   f <- h ^ b

a. O que seria um modelo da base de conhecimento apresentada? Apresente um modelo.

**R:** Um modelo de uma base de conhecimento é um conjunto de atribuição para os átomos de modo que nenhuma proposição seja dada como falsa.
O modelo mais simples para essa base é atribuir verdadeiro para todos os átomos.

b. Apresente uma interpretação que não seja um modelo da base de conhecimento apresentada.
**R:** Caso um fato tenha resultado falso, o modelo já não é válido, então atribuir falso à *b* ou *e* torna o modelo inválido.

c. Mostre como uma prova botton-up funcionaria para esta base de conhecimento. Apresente todas as consequências lógica desta KB.
**R:**

   |Proposição Utilizada| Consequências Lógicas|
   |--------------------|----------------------|
   |         c          |         {c}          |
   |         e          |        {c, e}        |
   |       b <- c       |       {c, e, b}      |
   |      a <- b ^ c    |      {c, e, b, a}    |
   |   g <- a ^ b ^ c   |     {c, e, b, a, g}  |

Portanto um modelo encontrado pelo algoritmo é que os átomos *a, b, c, e, g* são verdadeiros e os outros são falsos

d. Apresente uma prova top-down para a pergunta ask g.
   |Proposição Utilizada|        Query         |
   |--------------------|----------------------|
   |         g          |         {g}          |
   |   g <- a ^ b ^ c   |     {a ^ b ^ c}      |
   |      a <- b ^ c    |    {b ^ c ^ b ^ c}   |
   |    Simplificando   |        {b ^ c}       |
   |       b <- c       |        {c ^ c}       |
   |    Simplificando   |          {c}         |
   |          c         |          { }         |