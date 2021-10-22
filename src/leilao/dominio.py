from src.leilao.excecoes import LanceInvalido


class Usuario:
    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def propor_lance(self, leilao, valor):
        if self._valor_valido(valor):
            lance = Lance(self, valor)
            leilao.receber_lance(lance)
            self.__carteira -= valor
        else:
            raise LanceInvalido("Saldo em carteira insuficiente!")

    def _valor_valido(self, valor):
        return valor <= self.__carteira

class Lance:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

class Leilao:
    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0
        self.menor_lance = 0

    def receber_lance(self, lance: Lance):
        if self._lance_valido(lance):
            if not self.__lances:
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise LanceInvalido('Lance Indevido!!!')

    @property
    def lances(self):
        return self.__lances.copy()

    def _possui_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise LanceInvalido("Usuario não pode realizar dois lances seguidos!!!")

    def _valor_maior_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True
        else:
            raise LanceInvalido("Lance atual inferior ao anterior!!!")

    def _lance_valido(self, lance):
        return not self._possui_lances() \
               or self._usuarios_diferentes(lance) \
               and self._valor_maior_anterior(lance)