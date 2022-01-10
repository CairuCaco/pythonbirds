class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
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

class Carro:
    def __init__(self, direçao, motor):
        self.motor = motor
        self.direçao = direçao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
         self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direçao(self):
        return self.direçao.valor

    def girar_a_direita(self):
        self.direçao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direçao.girar_a_esqueda()

if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    direçao = Direçao()
    print(direçao.valor)
    direçao.girar_a_direita()
    print(direçao.valor)
    direçao.girar_a_esqueda()
    print(direçao.valor)
    carro = Carro(direçao, motor)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    print(carro.calcular_direçao())
    carro.girar_a_direita()
    print(carro.calcular_direçao())
    carro.girar_a_esquerda()
    print(carro.calcular_direçao())
    carro.frear()
    print(carro.calcular_velocidade())