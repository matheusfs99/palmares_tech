from main import *

def test_soma():
    assert soma(2, 3) == 5

def test_multiplica():
    # Arrange
    n1 = 2
    n2 = 4

    # Act 
    result = multiplica(n1, n2)

    # Assert
    assert result == 8