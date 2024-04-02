from collections import UserDict


#A base class for record fields.
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

#A class for storing a contact name. Required field.
class Name(Field):
    def __init__(self, value):
        if value:   
            self.value = value
        else:
            raise ValueError("This name field is required!")

#A class for storing a phone number. Has format validation (10 digits).
class Phone(Field):
    def __init__(self, value):
        if self.validate_phone(value):
            self.value = value
        else:
            print("Invalid phone number: must have 10 digits")
    
    def validate_phone(self, phone):
        return phone.isdigit() and len(str(phone)) == 10

#A class for storing information about a contact, including name and contacts list.
class Record:
    '''
    Adding phone numbers.
    Deleting phone numbers.
    Editing phone numbers.
    Search for a phone number.
    '''

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
        
    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
    
    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(str(p) for p in self.phones)}"

#A class for storing and managing records.
class AddressBook(UserDict):
    '''
    Adding records.
    Search for records by name.
    Delete records by name.
    '''
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        else:
            return False

def main(): 
    book = AddressBook()
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    for name, record in book.data.items():
        print(record)
        
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")

    book.delete("Jane")
    

if __name__ == "__main__":
    main()