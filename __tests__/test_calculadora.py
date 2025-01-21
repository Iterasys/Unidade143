import pytest

from calculadora.calculadora import somar_dois_numeros,       \
                                    subtrair_dois_numeros,    \
                                    multiplicar_dois_numeros, \
                                    dividir_dois_numeros

from utils.utils import ler_csv

def test_somar_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_subtrair_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = -2

    # Act - Executa
    resultado_atual = subtrair_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_multiplicar_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 5
    num2 = 7
    resultado_esperado = 35

    # Act - Executa
    resultado_atual = multiplicar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

def test_dividir_dois_numeros():
    # AAA

    # Arrange - Configura
    num1 = 12
    num2 = 3
    resultado_esperado = 4

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual
    

def test_dividir_por_zero():
    # AAA

    # Arrange - Configura
    num1 = 12
    num2 = 0
    resultado_esperado = 'Não é possível dividir por zero'

    # Act - Executa
    resultado_atual = dividir_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

@pytest.mark.parametrize('num1, num2, resultado_esperado',[
    (5,7,12), #tupla
    (3,0,3),
    (-1,6,5),
    (-9,-2,-11),
    (0.5,0.25,0.75)
])
def test_somar_dois_numeros_lista(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vem da lista acima (parametrize)

    # Act - Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # Assert - Valida
    assert resultado_esperado == resultado_atual

@pytest.mark.parametrize('num1, num2, resultado_esperado',
      ler_csv('./fixtures/csv/massa_somar.csv')                   
)
def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):
    # AAA

    # Arrange - Configura
    # Dados vem da lista acima (parametrize)

    # Act - Executa
    resultado_atual = somar_dois_numeros(float(num1), float(num2))

    # Assert - Valida
    assert float(resultado_esperado) == resultado_atual