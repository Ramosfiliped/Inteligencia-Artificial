# Algoritmos
Implementação de algoritmos de consistencia das cláusulas formais

## Bottom-Up
**Input:**
```
KB: Base de Conhecimento
```
**Output**
Lista com átomos que obrigatoriamente devem ser verdadeiros
```
def BU(KB)
    C = {}
    repetir
        selecionar h <- a1 ^ ... ^ an em KB onde ∀i, ai ∈ C e h ∉ C
        C = C U {h}
    ate que nenhuma cláusula possa ser selecionada
    retorne C
```

## Top-Down
**Input:**
```
KB: Base de conhecimento
Query: Consulta se átomo ou expressão é consequência lógica
```
**Output**
Se uma consulta é consequência lógica das outras expressões 
**Algoritmo**
```
def TD(KB, Query)
    G = Query
    Repita
        Selecione um átomo a em G
        Escolha uma cláusula "a <- B" em KB onde "a" é a cabeça
        G = B U (G\{a})
    ate G = {}
    retorne Sim
```