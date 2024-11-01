def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Повідомлення, якщо аргументів недостатньо
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError  # Повідомлення, якщо аргументів недостатньо
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated with new phone {new_phone}."
    else:
        raise KeyError  # Повідомлення, якщо контакт не знайдено


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError  # Повідомлення, якщо відсутній аргумент
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        raise KeyError  # Повідомлення, якщо контакт не знайдено


@input_error
def show_all_contacts(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
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
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()