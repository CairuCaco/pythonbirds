class Motor:
    def __init__(self):
        self.velocidade = 0
    def acelerar(self):
        self.velocidade += 1
    def freiar(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)
        return

NORTE = 'Norte'
SUL ='Sul'
LESTE ='Leste'
OESTE ='Oeste'
class Direçao:
    rotaçao_para_a_direita= {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotaçao_para_a_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotaçao_para_a_direita[self.valor]
    def girar_a_esqueda(self):
        self.valor = self.rotaçao_para_a_esquerda[self.valor]




if __name__ == '__main__':
    carro = Motor()
    print(carro.velocidade)
    Motor.acelerar(carro)
    print(carro.velocidade)
    Motor.acelerar(carro)
    print(carro.velocidade)
    Motor.acelerar(carro)
    print(carro.velocidade)
    Motor.freiar(carro)
    print(carro.velocidade)