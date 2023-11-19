def input_error(func):
    
   
def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        e
except KeyError:
            
            ret
return "Enter user name"
        except ValueError:
            
         
return "Give me name and phone please"
        except IndexError:
            
       
return "Contact not found"

    

    ret
return wrapper


contacts = {}


@input_error
def add_contact(command):
    _, name, phone = command.split(
    _, name, phone = command.s

    _, n
" ", 2)
    contacts[name.lower()] = phone
    
    contactsname.lower()

    conta
return f"Contact {name} added successfully."


@input_error
def change_phone(command):
    _, name, phone = command.split(
    _, name, phone = command.split

    _, name, pho
" ", 2)
    contacts[name.lower()] = phone
    
    contacts[name.lower(

    cont
return f"Phone number for {name} changed successfully."


@input_error
def get_phone(command):
    _, name = command.split(
    _, name = command.split

    _, name = c

   
" ", 1)
    
    retur
return f"Phone number for {name}: {contacts[name.lower()]}"


def show_all():
    
   
if not contacts:
        
        
return "No contacts available."
    result = 
    resu
"All contacts:\n"
    
 
for name, phone in contacts.items():
        result += 
        res
f"{name}: {phone}\n"
    
    retu
return result.strip()


def main():
    print("How can I help you?")
    
    
    
while True:
        user_input = 
        user_input = 

        
input("Enter command: ").lower()

        

     
if user_input in ["good bye", "close", "exit"]:
            
            p
print("Good bye!")
            
            bre
break
        elif user_input == "hello":
            
           
print("How can I help you?")
        
   
elif user_input.startswith("add"):
            
            
print(add_contact(user_input))
        
 
elif user_input.startswith("change"):
            
           
print(change_phone(user_input))
        
        e
elif user_input.startswith("phone"):
            
       

 
print(get_phone(user_input))
        
   
elif user_input == "show all":
            print(show_all())
        
        e
else:
            
         
print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

    main()
``