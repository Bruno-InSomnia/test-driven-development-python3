from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    @mark.calcular_bonus
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # given
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_sobrenome_recebe_Bruno_Guerreiro_de_Queiroz_deve_retornar_Guerreiro_de_Queiroz(self):
        entrada = ' Bruno Guerreiro de Queiroz  '
        esperado = 'Guerreiro de Queiroz'

        bruno = Funcionario(entrada, '11/11/2000', 1111)
        resultado = bruno.sobrenome()

        assert resultado == esperado

    def test_quando_salario_100000_deve_retornar_90000(self):
        entrada = 100000
        esperado = 90000

        diretor = Funcionario('Paulo Bragança', '11/10/2000', entrada)
        diretor.decrescimo_salario()
        resultado = diretor.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        ana = Funcionario('Ana', '11/10/2000', entrada)
        resultado = ana.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_ExceptionError(self):
        with pytest.raises(Exception):
            entrada = 10000000

            ana_rica = Funcionario('Ana', '11/10/2000', entrada)
            resultado = ana_rica.calcular_bonus()

            assert resultado
