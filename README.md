# miniRPG
Um mini RPG de luta que fiz durante a faculdade para treinar os conceitos de POO e herança.

## Como funciona: 

Nosso rpg vai começar com uma classe Pessoa.

Quando eu criar p = Pessoa("felix",30), isso significa que p
é uma pessoa com o nome "felix" e 30 de vida.

Ao fazer p.get_vida(), devo retornar a vida atual da pessoa (ou
seja, 30)

Uma pessoa pode atacar a outra. Para isso, veja o exemplo:
>>> marcia = Pessoa('marcia',20)
>>> marcia.get_vida()
20
>>> claudius = Pessoa('claudius',22)
>>> claudius.get_vida()
22
>>> marcia.lutar_com(claudius)
>>> marcia.atacar()
>>> marcia.get_vida()
20
>>> claudius.get_vida()
15 #22-7

Ou seja, para atacar, precisamos usar o método lutar_com (que, no
caso, direciona os ataque de marcia para claudius, veja a linha 
>>> marcia.lutar_com(claudius)) 

E depois disso, o método atacar (chamando 
>>> marcia.atacar(), ela ataca o claudius, tirando 7 de vida dele)

O dano nesse caso foi 7, mas esse número vai variar de acordo com a arma (que
vamos escolher no próximo teste)

Uma pessoa pode mudar de arma, dando danos diferentes.

a arma 'bola de fogo' dá 10 de dano
a arma 'soco' dá 2 de dano
a arma 'adaga' dá 7 de dano
a arma 'espada' dá 10 de dano

Para trocar de arma, devemos rodar
>>> marcia.selecionar_arma('soco')

Nesse caso, o adversário passa a tomar 2 de dano
>>> claudius.get_vida()
15
>>> marcia.atacar()
>>> claudius.get_vida()
13

Pessoas não podem ter vida negativa. O mínimo é 0. 

Se ela tiver 4 de vida e perder 10, fica com 0
Se ela tiver 0 de vida, e perder 5, continua com 0

"Pessoa" é um tipo de personagem muito genérico!

Por isso criei também um Mago. Magos têm as mesmas funcionalidades de pessoa:
* m = Mago("merlin",100) cria um mago chamado merlin, com 100 de vida
* m.get_vida, m.selecionar_arma, m.lutar_com funcionam do mesmo jeito.

Mago tem algumas diferenças com uma Pessoa genérica:
* Seu ataque com adaga é mais fraco: dá apenas 5 de dano
* Seu ataque com espada dá 0 de dano
* Por padrão, ele ataca com a bola de fogo (ou seja, se não dermos m.selecionar_arma, a arma dele é a bola de fogo)
* Magos resistem a fogo. Se forem atacados com 'bola de fogo', o dano é reduzido de 10 para 1
* Se você não passar um valor de vida pro mago, ele automaticamente tem 100 de vida

Criei mais uma classe, chamada Lutador.

Ele é igual a Pessoa, a menos das seguintes coisas:

* Sua arma padrão é a espada 
* Quando ele leva um soco, ele toma apenas 1 de dano

Outra classe, é o barbaro.

Ele é também é igual a Pessoa, a menos das seguintes coisas:

* Sua arma padrão é a espada 
* Se ele está machucado (sua vida atual é menor do que a inicial) os próximos ataque dele dão o dobro de dano
* Ele não sabe atacar com a bola de fogo (bolas de fogo dão 0 de dano, se ele tentar usar)

Se um Lutador um Barbaro ou uma Pessoa (qualquer um que não seja um Mago!) tentar
usar uma bola de fogo, ele se machuca, tomando 20 de dano

Todas as classes (Pessoa, Lutador, Mago, Barbaro) ganham um método curar, que as devolve para a vida completa (a vida que elas tinham no momento que foram criadas)

Repare que o Bárbaro perde a vantagem de dar mais dano se ele está curado

Todas as classes ganham um metodo envenenar e um método tomar_antidoto.

Ao chamar merlin.envenenar(), merlin fica envenenado.

Um personagem envenenado toma 10 de dano a cada ataque que ele FAZ. O antidoto remove o veneno.

O Bárbaro, porém, não sofre os efeitos do veneno

(as regras e o modo de jogo foram criadas pelo meu professor, eu apenas fiz o codigo.)

FIM!
