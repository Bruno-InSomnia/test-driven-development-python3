from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, value):
        self._salario = value

    def _confere_se_eh_diretor_ou_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and self.sobrenome() in sobrenomes

    def decrescimo_salario(self):
         if self._confere_se_eh_diretor_ou_socio():
            value = self.salario * 0.9
            self.salario = value

    def idade(self):
        data_nascimento_fatiada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_fatiada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_fatiado = nome_completo.split(' ')
        sobrenome_completo = ' '.join(nome_fatiado[1:])
        return sobrenome_completo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'


