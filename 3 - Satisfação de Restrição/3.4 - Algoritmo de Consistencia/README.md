# Algoritmo de Consistência
Apesar de a busca em profundidade sobre o espaço de busca de atribuições ser normalmente uma melhor substancial sobre o algoritmo generate-and-test, ele ainda continua tendo várias ineficiências que podem surgir.

Os algoritmos de consistência são melhor pensado como operando sobre a rede de restrições formada pelo CSP:
* Existem um nó para cada variável;
* Existe um nó para cada restriçã;
* Associado a cada variável **X**, tem um **Dx** de valores possíveis. Esse conjunto de valores inicialmente é o domínio da variável;
* Para cada restrição *c*, e para cada variável *X* no escopo de *c*, existe um arco <*X*, *c*>.

Essa rede é chamada de **rede de restrições**.

No caso mais simples, quando uma restrição tem apenas uma variável no escopo, o arco é **domínio de consistência** se todo valor da variável satisfaz a restrição.

Suponha uma restrição *c* que tenha escopo *{X, Y1, ..., Yk}*. O arco *<X, c>* é um arco consistente se, para cada valor de *x* ∈ *Dx*, existe um valor *y1, ..., yk* onde *yi* ∈ *Dy*, em que *c(X = x, Y1 = y1, ..., Yk = yk)* é satisfeito. A rede é consistente se todos os seus arcos são consistentes.

Se um arco <*X, c*> não é consistente, existe um algum(ns) valor(es) de *X* em que não existe valores para *Y* que satisfaça a restrição.

## Algoritmo de Consistência
**Entrada:**
* Vs: Variáveis
* dom: Domínio de cada variável
* Cs: Restrições

**Saída:**
Lista com valores possíveis para cada variável
```
def GAC(<Vs, dom, Cs>)
    retorne GAC2(<Vs, dom, Cs>, {<X, c> | c ∈ Cs ^ X ∈ escopo(c)})

def GAC2(<Vs, dom, Cs>, to_do)
    enquanto  to_do ≠ {}
        selecione e remova <X, c> from to_do
        {Y1, ..., Yk} := escopo(c) \ {X}
        ND := {x | x ∈ dom(X) ^ existe y1 ∈ dom(Y1) ... yk ∈ dom(Yk) tal que c(X = x, Y1 = y1, ..., Yk = yk)}
        se ND ≠ dom(X) então
            todo := todo U {<Z, c'> | {X, Z} ⊆ escopo(c'), c' ≠ c, Z ≠ X}
            dom(X) := ND
    retorne dom
```

O algoritmo de **consistência de arcos generalizado (GAC)** é dado acima. Ele faz toda a rede ser consistente por considerar uma série de conjuntos *to_do* de potenciais arcos inconsistentes.
O conjunto *to_do* inicialmente consiste em todos os arcos no grafo. Enquanto o conjunto não está vazio, um arco <X,c> é removido do conjunto e considerado.
Se o arco é um arco não consistente, ele tem seu domínio podado dentro do domínio de *X* para que seja consistente.
Todos os arcos consistentes que podem, por caus da poda de *X*, terem se tornado insconsistentes são colocados de volta no conjunto *to_do*. Estes são os arcos <*Z, c'*>, onde *c'* é uma restrição diferente da restrição *c* que envolve a variável *X*, e *Z* é a variável envolvida em *c'* sem ser *X*.
