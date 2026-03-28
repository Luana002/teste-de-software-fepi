import pytest

from src import sistema_locacao


@pytest.fixture(autouse=True)
def limpar_estado():
    sistema_locacao.clientes.clear()
    sistema_locacao.veiculos.clear()
    yield
    sistema_locacao.clientes.clear()
    sistema_locacao.veiculos.clear()


@pytest.fixture
def app_module():
    import app as app_module

    app_module.resetar_dados()
    app_module.app.config["TESTING"] = True
    return app_module


@pytest.fixture
def client(app_module):
    with app_module.app.test_client() as test_client:
        yield test_client
