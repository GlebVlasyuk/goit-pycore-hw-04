import sys
from pathlib import Path

from colorama import Fore, Style, init


def print_directory_tree(directory: Path, prefix: str = "") -> None:
    try:
        entries = sorted(
            directory.iterdir(),
            key=lambda item: (item.is_file(), item.name.lower()),
        )
    except OSError as error:
        print(f"{prefix}{Fore.RED}[ERROR]{Style.RESET_ALL} {error}")
        return

    for index, entry in enumerate(entries):
        is_last = index == len(entries) - 1
        branch = "`-- " if is_last else "|-- "
        child_prefix = "    " if is_last else "|   "

        if entry.is_dir():
            print(f"{prefix}{branch}{Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
            print_directory_tree(entry, prefix + child_prefix)
        else:
            print(f"{prefix}{branch}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


def main() -> None:
    init(autoreset=True)

    if len(sys.argv) != 2:
        print(f"Usage: python {Path(sys.argv[0]).name} /path/to/directory")
        sys.exit(1)

    directory = Path(sys.argv[1]).expanduser().resolve()

    if not directory.exists():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path does not exist.")
        sys.exit(1)

    if not directory.is_dir():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} Path is not a directory.")
        sys.exit(1)

    print(f"{Fore.CYAN}{directory.name}{Style.RESET_ALL}/")
    print_directory_tree(directory)


if __name__ == "__main__":
    main()
