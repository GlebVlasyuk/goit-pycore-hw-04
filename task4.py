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


def update_contact(args: list[str], contacts: dict[str, str]) -> str:
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


def show_contact_by_phone(phone: str, contacts: dict[str, str]) -> str:
    for name, saved_phone in contacts.items():
        if saved_phone == phone:
            return f"{name}: {saved_phone}"
    return "Contact not found."


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
            if len(args) == 0:
                name = input("Enter name: ").strip()
                phone = input("Enter phone: ").strip()
                args = [name, phone]
            elif len(args) == 1:
                phone = input("Enter phone: ").strip()
                args = [args[0], phone]

            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            search_type = input("Search by phone or name? ").strip().lower()

            if search_type == "name":
                name = args[0] if len(args) == 1 else input("Enter name: ").strip()
                print(show_phone([name], contacts))
            elif search_type == "phone":
                phone = args[0] if len(args) == 1 else input("Enter phone: ").strip()
                print(show_contact_by_phone(phone, contacts))
            else:
                print("Invalid command.")
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
