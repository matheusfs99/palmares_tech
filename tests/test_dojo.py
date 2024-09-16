''''
O ano for divisível por 4, 
mas não divisível por 100, 
exceto se ele for também divisível por 400.
'''
from dojo import *

def test_divisivel_por_4():
    ano = 2024
    resposta = bissexto(ano)
    esperado = True

    assert resposta == esperado

def test_anos_bissexto_puzzle():
    assert bissexto(1600) == True
    assert bissexto(1732) == True
    assert bissexto(1888) == True
    assert bissexto(1944) == True
    assert bissexto(2008) == True

def test_anos_bissexto_puzzle():
    assert bissexto(1600) == True
    assert bissexto(1732) == True
    assert bissexto(1888) == True
    assert bissexto(1944) == True
    assert bissexto(2008) == True

def test_anos_nao_bissexto_puzzle():
    assert bissexto(1742) == False
    assert bissexto(1889) == False
    assert bissexto(1951) == False
    assert bissexto(2011) == False