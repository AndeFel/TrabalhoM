from contador import contar_palavras

def test_contar_palavras():
    assert contar_palavras("Olá mundo") == 2
    assert contar_palavras("Isso é um teste") == 4
    assert contar_palavras("") == 0
    assert contar_palavras("Python é incrível") == 3
