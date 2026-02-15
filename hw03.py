import sys
from pathlib import Path

from colorama import Fore, Style, init


def show_tree(folder_path, indent=""):
    try:
        items = list(folder_path.iterdir())
        items.sort(key=lambda x: x.name.lower())
    except OSError as error:
        print(f"{indent}{Fore.RED}Cannot read directory: {error}{Style.RESET_ALL}")
        return

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        branch = "`-- " if is_last else "|-- "
        next_indent = indent + ("    " if is_last else "|   ")

        if item.is_dir():
            print(f"{indent}{branch}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
            show_tree(item, next_indent)
        else:
            print(f"{indent}{branch}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main():
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"Usage: python {Path(sys.argv[0]).name} /path/to/directory")
        sys.exit(1)

    folder = Path(sys.argv[1]).expanduser().resolve()

    if not folder.exists():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path does not exist.")
        sys.exit(1)

    if not folder.is_dir():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path is not a directory.")
        sys.exit(1)

    print(f"{Fore.CYAN}{folder.name}{Style.RESET_ALL}/")
    show_tree(folder)


if __name__ == "__main__":
    main()
