import pytest
from src.database import DatabaseConnection
from src.calculator import Calculator

# Fixture para o banco de dados
@pytest.fixture
def db():
    # Setup: Cria a conexão antes do teste rodar
    database = DatabaseConnection()
    yield database  # Entrega o banco para o teste usar
    
    # Teardown: Desconecta automaticamente após o teste terminar
    database.disconnect()

# Fixture para a calculadora
@pytest.fixture
def calc():
    return Calculator()