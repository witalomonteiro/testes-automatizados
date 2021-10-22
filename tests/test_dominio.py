from unittest import TestCase
from src.leilao.dominio import Lance, Leilao, Usuario
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.leilao_teste = Leilao("Cavalo")
        self.witalo = Usuario("Witalo", 1000)
        self.witalo.propor_lance(self.leilao_teste, 500)

    # 001 - Quando os lances foram realizados de forma crescente
    def test_lances_ordem_crescente(self):
        monteiro = Usuario("Monteiro", 1000)
        monteiro.propor_lance(self.leilao_teste, 750)

        menor_valor_esperado = 500
        maior_valor_esperado = 750

        self.assertEqual(menor_valor_esperado, self.leilao_teste.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao_teste.maior_lance)

    # 002 - Quando os lances forem realizados de forma decrescente
    def test_lances_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            monteiro = Usuario("Monteiro", 1000)
            monteiro.propor_lance(self.leilao_teste, 250)

    # 003 - Quando for realizado um unico lance
    def test_um_lance(self):
        menor_valor_esperado = 500
        maior_valor_esperado = 500

        self.assertEqual(menor_valor_esperado, self.leilao_teste.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao_teste.maior_lance)

    # 004 - Quando for realizado tres lances
    def test_tres_lances(self):
        monteiro = Usuario("Monteiro", 1000)
        jose = Usuario("José", 1000)
        monteiro.propor_lance(self.leilao_teste, 750)
        jose.propor_lance(self.leilao_teste, 800)

        menor_valor_esperado = 500
        maior_valor_esperado = 800

        self.assertEqual(menor_valor_esperado, self.leilao_teste.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao_teste.maior_lance)

    # 005 - Quando o leilão não tiver nenhum lance
    def test_leilao_sem_lances(self):
        quantidade_lances = len(self.leilao_teste.lances)
        self.assertEqual(1, quantidade_lances)

    # 006 - Quando o usuario anterior for diferente, permitir um novo lance
    def test_lance_anterior_usuario_diferente(self):
        monteiro = Usuario("Monteiro", 1000)
        monteiro.propor_lance(self.leilao_teste, 750)
        quantida_lances = len(self.leilao_teste.lances)
        self.assertEqual(2, quantida_lances)

    # 007 - Quando o usuario anterior for igual, não permitir um novo lance
    def test_lance_anterior_usuario_igual(self):
        with self.assertRaises(LanceInvalido):
            self.witalo.propor_lance(self.leilao_teste, 500)
            self.witalo.propor_lance(self.leilao_teste, 750)
