from src.main import page

def test_basic_action() -> None:
    test_page = page(7)

    for i in range(3):
        test_page.pagination_action('next')
    
    for i in range(2):
        test_page.pagination_action('previous')

    if test_page.display == "1 (2) 3 4 5 6 7":
        assert True
    else:
        print (test_page.display)
        assert False


def test_basic_doesnt_pass_max() -> None:
    test_page = page(7)

    for i in range(10):
        test_page.pagination_action('next')

    if test_page.display == "1 2 3 4 5 6 (7)":
        assert True
    else:
        print (test_page.display)
        assert False

def test_basic_doesnt_pass_min() -> None:
    test_page = page(7)

    for i in range(5):
        test_page.pagination_action('next')

    for i in range(10):
        test_page.pagination_action('previous')

    if test_page.display == "(1) 2 3 4 5 6 7":
        assert True
    else:
        print (test_page.display)
        assert False

def test_partII() -> None:
    test_page = page(100)
    test_page2 = page(9)

    for i in range(41):
        test_page.pagination_action('next')
    
    for i in range(4):
        test_page2.pagination_action('next')

    if test_page.display == "1 ... 41 (42) 43 ... 100":
        assert True
    else:
        print("42 of 100: \n")
        print (test_page.display)
        assert False

def test_loop() -> None:
    answers = [
        "(1) 2 3 4 5 ... 9",
        "1 (2) 3 4 5 ... 9",
        "1 2 (3) 4 5 ... 9",
        "1 2 3 (4) 5 ... 9",
        "1 ... 4 (5) 6 ... 9",
        "1 ... 5 (6) 7 8 9",
        "1 ... 5 6 (7) 8 9",
        "1 ... 5 6 7 (8) 9",
        "1 ... 5 6 7 8 (9)"
    ]

    test_page = page(9)

    for i in range(1,9):
        test_page.pagination_action('next')
        if test_page.display == answers[i]:
            assert True
        else:
            print(f"{i} of 9: \n")
            print (test_page.display)
            assert False
