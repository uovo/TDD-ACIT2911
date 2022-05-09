from utils import names

def test_two_names():
    assert names.split_name("Walter Anelko") == ["Walter", "Anelko"]

def test_middle_names():
    assert names.split_name("Walter Pavel Anelko") == ["Walter Pavel", "Anelko"]
    assert names.split_name("Walter Pavel Anelko Smith") == ["Walter Pavel Anelko", "Smith"]

def test_surname_prefixes():
    assert names.split_name("Karina van der Nereus") == ["Karina", "van der Nereus"]
    assert names.split_name("Karina Alice van der Nereus") == ["Karina Alice", "van der Nereus"]

def test_split_name_onename():
    assert names.split_name("Anelko") == ["", "Anelko"]

def test_split_name_nonames():
    assert names.split_name("") == ["", ""]