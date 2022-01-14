from demo.main import pagarme, pagarme_mission


def test_pagar_me_mission():
    result = pagarme_mission()
    assert result == "Empoderar os negócios digitais do empreendedor Brasileiro."


def test_pagarme():
    result = pagarme()
    assert result == r"""Pagarme"""
