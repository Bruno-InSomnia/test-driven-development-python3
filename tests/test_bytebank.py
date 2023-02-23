from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # given
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # when

        assert resultado == esperado  # then

    def test_quando_sobrenome_recebe_Bruno_Guerreiro_de_Queiroz_deve_retornar_Guerreiro_de_Queiroz(self):
        entrada = ' Bruno Guerreiro de Queiroz  '
        esperado = 'Guerreiro de Queiroz'

        bruno = Funcionario(entrada, '11/11/2000', 1111)
        resultado = bruno.sobrenome()

        assert resultado == esperado

