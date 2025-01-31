class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome=None, idade=16):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls}-olhos{cls.olhos}'


class Homem(Pessoa):
    pass



if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.cumprimentar)
    print(luciano.nome)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(renzo.__dict__)
    luciano.olhos = 1
    Pessoa.olhos = 3
    del luciano.olhos
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonima')
    print(isinstance(pessoa ,Pessoa))
    print(isinstance(pessoa ,Homem))
    print(isinstance(renzo ,Pessoa))
    print(isinstance(renzo ,Homem))