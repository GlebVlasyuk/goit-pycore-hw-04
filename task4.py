def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.strip().split()
    if not parts:
        return "", []

    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 2:
        return "Invalid command."

    name, phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    if len(args) != 1:
        return "Invalid command."

    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all_contacts(contacts: dict[str, str]) -> str:
    if not contacts:
        return "No contacts saved."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")
    print("Available commands: hello, add, change, phone, all, close, exit")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
