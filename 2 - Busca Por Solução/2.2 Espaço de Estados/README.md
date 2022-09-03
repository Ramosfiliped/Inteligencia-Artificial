# Espaço de Estados
Um formulação geral de ações inteligentes é em termos de **espaço de estados**. Um **estado** contém toda informação necessário para predizer os efeitos de uma ação e determinar se um estado satisfaz o objetivo.

Busca em estados de espaço assume:
* O agente tem perfeito conhecimento sobre o espaço de estados e está planejando para o caso em que observa em que estado está: há total observabilidade
* O agente tem um conjunto de ações com efeitos determinísticos.
* Um agente pode determinar se um estado satisfaz o objetivo.

Uma **solução** é a sequência de ações que o agente executará do estado atual que alcança o estado objetivo.

Um **problema de estados de espaço** consiste em
* Um conjunto de estados;
* Um estado distinguível chamado **estado inicial**;
* Uma **função de ação** que, dado um estado e uma ação, retorna um novo estado;
* Um **objetivo** especificado como função booleana, goal(s), que é verdadeiro quando o estado *s* satisfaz o objetivo, nesse caso dizemos que *s* é o **estado objetivo**;
* um critério que especifica a qualidade de uma solução aceitável. Por exemplo, qualquer sequência de ações que leve o agente ao estado objetivo pode ser aceitável, ou pode haver custos associados às ações e o agente pode ser solicitado a encontrar uma sequência que tenha um custo total mínimo. Uma solução que é melhor de acordo com algum critério é chamada de **solução ótima**.