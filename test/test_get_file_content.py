from functions.get_file_content import get_file_content


def test_get_file_content():
    print(test_results(get_file_content("calculator", "lorem.txt")))
    print(test_results(get_file_content("calculator", "main.py")))
    print(test_results(get_file_content("calculator", "pkg/calculator.py")))
    print(
        test_results(get_file_content("calculator", "/bin/cat"))
    )  # (this should return an error string)
    print(
        test_results(get_file_content("calculator", "pkg/does_not_exist.py"))
    )  # (this should return an error string)


def test_results(result: tuple[str, bool]):
    print(result[0])
    print(f"lorem.txt length: {len(result[0])}")
    print(f"lorem.txt truncated: {result[1]}")


test_get_file_content()
