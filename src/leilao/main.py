from dominio import Usuario, Lance, Leilao


leilao_teste = Leilao("Cavalo")

witalo = Usuario("Witalo", 1000)
monteiro = Usuario("Monteiro", 1000)

print(witalo.carteira)
print(monteiro.carteira)

witalo.propor_lance(leilao_teste, 500)
monteiro.propor_lance(leilao_teste, 550)

print(witalo.carteira)
print(monteiro.carteira)

print(f"Maior Lance: {leilao_teste.maior_lance} e Menor Lance: {leilao_teste.menor_lance}")

### HINTS ###
# Ctrl + Shift + T >>> Atalho para criar novo teste
# Alt + Enter >>> Atalho p/ importar libs
# Ctrl + P >>> Atalho p/ exibir balão com dica de parametros
# Ctrl + Shift + Direcional Cima ou Baixo >>> Move a linha de codigo
# assert (pytest) >>> Validar testes de sucesso
# with pytest.raises() (pytest) >>> Validar testes de falha
# assertEqual() (TestCase class from unittest lib) >>> Validar testes de sucesso
# with self.assertRaises() (TestCase class from unittest lib) >> Validar testes de falha