import pytest
import conftest
from pages.lupa import LupaPage


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
    def test_ExibirCampoBusca(self):
        browser = conftest.browser
        novaLupa = LupaPage()
        novaLupa.acessar_lupa()
