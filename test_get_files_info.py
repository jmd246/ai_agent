from functions.get_files_info import get_files_info

def run_test():
    print(get_files_info("calculator", "."))
    print(get_files_info("calculator", "/bin"))
    print(get_files_info("calculator", "../"))
    print(get_files_info("calculator", "main.py"))

run_test()