class Pessoa():
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        self.vida_inicial = vida

        self.selecionar_arma("adaga")

        self.isMago = False
        self.isLutador = False
        self.isBarbaro = False
        self.isEnvenenado = False

        self.danos = {
            "adaga":7,
            "soco":2,
            "espada":10,
            "bola de fogo":10
        }

    def curar(self):
        self.vida = self.vida_inicial

    def envenenar(self):
        self.isEnvenenado = True
        
    def tomar_antidoto(self):
        self.isEnvenenado = False

    def get_vida(self):
        return self.vida

    def lutar_com(self,oponente):
        self.oponente = oponente

    def atacar(self):
        dano = self.danos[self.arma]

        if self.arma == 'bola de fogo' and not self.isMago:   
            self.vida -= 20

        if self.oponente.isMago and self.arma == 'bola de fogo':
            if self.isBarbaro:
                dano = 0
            else:
                dano=1

        if self.oponente.isLutador and self.arma == 'soco':
            dano = 1

        if self.isBarbaro:
            if self.vida < self.vida_inicial:
                dano *= 2

        if self.isEnvenenado == True and not self.isBarbaro:
            self.vida -= 10

        self.oponente.vida -= dano
        if self.oponente.vida <0:
            self.oponente.vida = 0
    
    def selecionar_arma(self,arma):
        self.arma = arma

class Mago(Pessoa):
    def __init__(self, nome, vida = 100):
        super().__init__(nome, vida)
        self.danos['adaga'] = 5
        self.danos['espada'] = 0
        self.isMago = True

        self.selecionar_arma('bola de fogo')

class Lutador(Pessoa):
    def __init__(self, nome, vida = 100):
        super().__init__(nome, vida)
        self.isLutador = True

        self.selecionar_arma('espada')

class Barbaro(Pessoa):
    def __init__(self, nome, vida = 100):
        super().__init__(nome, vida)
        self.isBarbaro = True

        self.selecionar_arma('espada')
        
        
