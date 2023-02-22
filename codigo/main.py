from codigo.bytebank import Funcionario


def test_idade():
    funcionario_test = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_test.idade()}')

test_idade()