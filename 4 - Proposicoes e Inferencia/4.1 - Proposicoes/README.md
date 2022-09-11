# Proposições
Declarações sobre o mundo fornecem restrições sobre o que pode ser verdade. Restrições podem especificar extensionalmente como tabelas de atribuições válidas às variáveis, ou intencionalmente em termo de fórmulas.

Existe um número de razões para usar proposições para especificar restrições e consultas
* É normalmente mais conciso e legível entregar uma declaração lógica sobre as relações entre variáveis que usar uma representação extensional.
* A forma de conhecimento pode ser explorada para tornar o raciocínio mais eficiente
* Elas são modulares, então pequenas mudanças no problema resulta em pequenas mudanças no base de conhecimento
* O tipo de consulta que um agente deve ter que fazer para responder pode ser mais rica que uma única atribuição de valores à variáveis.
* Essa linguagem é extendida para raciocinar sobre indivíduos e relações.


## Sintaxe do cálculo proposicional
Uma **proposição** é uma sentença, escrita em uma linguagem, que tem uma veracidade (ou seja, pode ser verdadeiro ou falso) no mundo. Uma proposição é construída por proposições atômicas usando conectores locais.

Uma **proposição atômica**, ou apenas **átomo**, é um símbolo. Usamos a convenção que proposições consistem de letras, dígitos e underscore (_) e começa com uma letra minúscula.

Proposições podem ser construídas de proposições mais simples usando conectores lógicos. Uma **proposição** ou **fórmula lógica** é também 
* uma proposição atômica or
* uma **proposição composta** na forma
  
| ¬p     | não p            | negação de p         |
|--------|------------------|----------------------|
| p ^ q  | p e q            | conjunção de p e q   |
| p v q  | p ou q           | disjunção de p e q   |
| p -> q | p implica q      | implicação de p em q |
| p <-> q| p se somente se q| equivalência de p e q|
Onde *p* e *q* são proposições.

Os operadores ¬, ^, v, ->, <-> são **conectores lógicos**


## Semântica do cálculo proposicional
**Semânticas** definem o significado da sentença de uma linguagem. Quando as sentenças são sobre o mundo, semânticas especificam como colocar símbolos da linguagem em correspondência com o mundo.

Uma **interpretação** consistem de uma função π que papeia os átomos para **{true, false}**. Se π(a) = verdadeiro, o átomo *a* é verdadeiro na interpretação.

Um **base de conhecimento** é um conjunto de proposições que são definidos para serem verdadeiro. Um elemento do base de conhecimento é um **axioma**.

Um **modelo** de um base de conhecimento *KB* é uma interpretação em quais proposições KB é verdadeiro.

Se *KB* é um base de conhecimento e *g* uma proposição, *g* é **consequência lógica** de *KB*, escrito como

KB ⊧ g
	
se *g* é verdadeiro em todo modelo de *KB*.
Portanto KB ⊧/ g, significa que *g* não é consequência lógica de *KB*, onde existe um modelo de *KB* em que *g* é falso. 

A metodologia para moldar uma base de conhecimento para representar um mundo pode ser expressada da seguinte forma:
1. O modelador de base de conhecimento escolhe um domínio da tarefa ou mundo para representar, em que é a interpretação pretendida. Isso pode ser algum aspecto do mundo real, ou laboratório em particular.
2. O modelador seleciona átomos para representar proposições de interesse. Cada átomo tem um significado preciso respeitando a interpretação pretendida;
3. O modelador **informa** as proposições do sistema que são verdadeiras na interpretação pretendida. Isso é normalmente chamado de **domínio axiomático**, onde as proposições dadas são **axiomas** do domínio.
4. O modelador pode agora **perguntar** sobre a interpretação pretendida. Ele é capaz de interpretar as respostas usando o significado assimilado a cada símbolo.