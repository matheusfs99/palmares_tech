''''
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:

Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:

Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
'''
from dojo2 import *

def test_caixa100():
    saldo = 100
    resultado = caixa(saldo)
    resultado_esperado = {100: 1}
    assert resultado == resultado_esperado

def test_caixa30():
    saldo = 30
    resultado = caixa(saldo)
    resultado_esperado = {20: 1, 10:1}
    assert resultado == resultado_esperado

def test_caixa50():
    saldo = 50
    resultado = caixa(saldo)
    resultado_esperado = {50: 1}
    assert resultado == resultado_esperado

def test_caixa10():
    saldo = 10
    resultado = caixa(saldo)
    resultado_esperado = {10: 1}
    assert resultado == resultado_esperado