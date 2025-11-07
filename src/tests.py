from src.wordsearch import WordSearch


def test_1():
    grid = "abcdefghijklmnopqrstuvwxy"

    ws = WordSearch(grid)

    test_cases = {
        "abcd": True,
        "fghi": True,
        "klmno": True,
        "afkpu": True,
        "bgqv": False,
        "xyza": False,
        "mnop": False,
        "qrst": True
    }

    for word, expected in test_cases.items():
        result = ws.is_present(word)
        assert result == expected, f"Test failed for word '{word}': expected {expected}, got {result}"

    print("All test cases passed!")


def test_2():
    grid = (
        "abcdefghij"
        "klmnopqrst"
        "uvwxyzabcd"
        "efghijklmn"
        "opqrstuvwx"
        "yzabcdefgh"
        "ijklmnopqr"
        "stuvwxyzab"
        "cdefghijkl"
        "mnopqrstuv"
    )

    test_cases = {
        "abcd": True,
        "klmn": True,
        "mnop": True,
        "wxyz": True,
        "uvwx": True,
        "ijklmnop": True,
        "aeim": False,
        "bfjn": False,
        "qrst": True,
        "mnopq": True,
        "vwxy": True,
        "yzab": True,
        "abcdij": False,
        "mnopxyz": False,
    }

    ws = WordSearch(grid)

    for word, expected in test_cases.items():
        result = ws.is_present(word)
        assert result == expected, f"Test failed for word '{word}': expected {expected}, got {result}"

    print("All tests passed!")


from src.wordsearch import WordSearch


def test_3():
    grid = (
        "abcdefghijklmno"
        "pqrstuvwxyzabcd"
        "efghijklmnopqrs"
        "tuvwxyzabcdefgk"
        "hijklmnopqrstuv"
        "wxyzabcdefghijk"
        "lmnopqrstuvwxyb"
        "zabcdefghijklmq"
        "nopqrstuvwxyzac"
        "cdefghijklmnopd"
        "rstuvwxyzabcdep"
        "ghijklmnopqrstf"
        "wxyzabcdefghijg"
        "lmnopqrstuvwxyh"
        "zabcdefghijklmj"
    )

    ws = WordSearch(grid)

    test_cases = {
        "abcd": True,
        "mnopq": True,
        "wxyz": True,
        "ijklmnop": True,
        "stuv": True,
        "abcdefgh": True,
        "apethw": True,
        "bqfuix": True,
        "cdpfghj": True,
        "aeim": False,
        "bfjn": False,
        "mnopxyz": False,
        "xyzabce": False,
    }

    for word, expected in test_cases.items():
        result = ws.is_present(word)
        assert result == expected, f"Test failed for word '{word}': expected {expected}, got {result}"

    print("All square grid test cases passed!")


test_1()
test_2()
test_3()
