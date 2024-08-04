from twttr import shorten


def test_shorten():
    assert shorten("amir") == "mr"
    assert shorten("wnt") == "wnt"
    assert shorten("wn2t") == "wn2t"
    assert shorten("AmIr") == "mr"
    assert shorten("a@m!!ir") == "@m!!r"
