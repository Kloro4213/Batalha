# Batalha
Simulador de batalha pra um jogo que não existe ainda

Estarei programando em python porque é rápido e possível de ser feito durante os períodos ociosos no meu estágio. Assim que terminado, eu o usarei como experimentação prática para balanceamento do jogo e inspiração para criar conteúdo. O plano final é criar o jogo com c#, na unity.

Resumindo muito, a luta se passa num campo 7x7, onde cada casa ganha uma carta no início das rodadas. Daí, ambos jogador e inimigo se alternam movimentando-se em turnos, coletando as cartas das casas que visitarem. 
Assim que onze turnos se passarem, a luta passa pra fase de batalha, na qual os lutadores usam as cartas que coletaram no decorrer de cinco rodadas. Em cada rodada da batalha, os participantes escolhem duas das cartas coletadas, uma com a face para cima, e outra para baixo. Quando todos já tiverem escolhido um par de cartas, elas se resolvem. Cartas viradas para baixo são consumidas, as viradas para baixo não. A batalha sempre tem cinco rodadas, independente de qualquer coisa.


Comandos Existentes:
  * IJ - Invocar Jogador
  * II - Invocar Inimigo
  * IT - Invocar Todos (em casas aleatórias)
  * CJ - Começar Jogo
  * XX - Fechar Jogo


Expandirei um pouco melhor abaixo:

Existirão 3 baralhos existentes em cada partida. O baralho do jogador, o baralho do inimigo e o baralho do ambiente.
No início da batalha e sempre que começa a fase de movimentação, cada casa recebe uma carta escolhida aleatoriamente entre cartas sortidas dos baralhos citados ou uma carta branca. As chances são de 25% para cada
Cada personagem terá atributos para mediar o decorrer do combate, seu respectivo baralho e também uma coleção de movimentos básicos. Esses movimentos básicos são "cartas" de cada tipo com efeitos simples.
Os tipos de cartas são:

 * Manobras - Cartas oportunistas de efeitos sutis
    (defensivas, especialistas, punitivas)
 * Golpes - Cartas que representam agressão rápida e direta
    (ataques, investidas, interrupções)
 * Talentos - Cartas de poder absoluto e superioridade opressora
    (Evoluções, Efeitos especiais, Enfraquecer o alvo)

Ou seja, cada personagem tem três movimentos básicos. Um pra cada tipo
Tentar pegar a carta de um inimigo te dará ao invés disso a tua versão de movimento básico. O contrário também é verdade, se um inimigo pegar uma carta do jogador, ele obterá a versão dele de movimento básico do mesmo tipo da carta obtida.
Cartas brancas são basicamente cartas coringas para movimento básico. 

No início da fase de movimentação, ambos personagens já recebem uma carta aleatória para compensar pela casa que já estão ocupando.

Um detalhe importante na fase de movimentação é que algumas vantagens são distribuídas aos personagens dependendo da ordem dos turnos
O primeiro a se mover anda uma casa adicional, o que acaba dando a ele sete cartas no final de tudo
O segundo a se mover pode se mover diagonalmente uma vez durante a fase de movimentação.

Na fase de combate, os dois personagens entram numa luta, não importa onde estejam
cada personagem tem uma barra de vida e uma barra de mente. A partida inteira termina quando um dos personagens tem a sua vida reduzida a 0. 
Nesta fase, cada personagem se alterna em turnos colocando as suas cartas. Aquele que se moveu primeiro na fase de movimentação será o primeiro a escolher cartas 
As cartas se resolvem simultaneamente em pares. Em questão de ordem absoluta, manobras são mais rápidas que golpes que são mais rápidos que talentos

A barra de mente será explicada futuramente, mas ela tem interferência direta em múltiplos aspectos do combate.

Quando os cinco turnos do combate acabam, uma nova fase de movimentação começa. Cada personagem tem a opção de cair numa casa aleatória ou voltar na casa que pararam. Casas que não foram visitadas mantêm suas cartas, e casas sem cartas recebem cartas novas. Cartas não usadas no combate permanecem com o personagem, mas todos têm um limite de dez cartas para se ter.