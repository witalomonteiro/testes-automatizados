import pytest

from src.leilao.dominio import Usuario, Leilao
from src.leilao.excecoes import LanceInvalido


@pytest.fixture
def leilao():
    return Leilao('Smartphone')

@pytest.fixture
def usuario():
    return Usuario("Barros", 1000)

# 001 - Quando propor lance, valor deve ser substituido da carteira do usuario
def test_propor_lance(leilao, usuario):
    usuario.propor_lance(leilao, 500)
    assert usuario.carteira == 500

# 002 - Quando propor lance com valor menor que saldo em carteira de usuario
def test_propor_lance_menor_carteira(leilao, usuario):
    usuario.propor_lance(leilao, 999)
    assert usuario.carteira == 1

# 003 - Quando propor lance com valor igual ao saldo em carteira de usuario
def test_propor_lance_igual_carteira(leilao, usuario):
    usuario.propor_lance(leilao, 1000)
    assert usuario.carteira == 0

# 004 - Quando propor lance com valor maior ao saldo em carteira de usuario
def test_propor_lance_maior_carteira(leilao, usuario):
    with pytest.raises(LanceInvalido):
        usuario.propor_lance(leilao, 1500)