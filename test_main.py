import main

def test_greet():
    assert main.greet("World") == "Hello, Test!"


if __name__ == "__main__":
    import pytest

    ret = pytest.main(["-v", "--max-fail=1"])
    if ret == 0:
        print("Testy zakonczone pomyslnie")
    else:
        print("cos sie popsulo")