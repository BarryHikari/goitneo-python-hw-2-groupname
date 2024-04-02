def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        #all commands
        except TypeError:
            return "Invalid command. Please provide necessary arguments."
        #show_phone
        except ValueError as e:
            return "Give me name and phone please."
        except KeyError as e:
            return f"No contact found with the name: {e}"
        except IndexError as e:
            return "Missing command parameters."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except KeyError:
        return None, None

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        raise KeyError(name)
    #if name in contacts.keys():
    else:
        return contacts[name]


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError(name)
        
@input_error
def show_all(contacts):
    if contacts:
        messages = []
        for name, phone in contacts.items():
            message = f"{name}: {phone}"
            messages.append(message)
        return "\n".join(messages)
    else:
        return "The list of contacts is empty!"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
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
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()