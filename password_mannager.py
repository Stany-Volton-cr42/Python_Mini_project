from cryptography.fernet import Fernet

# it will convert key + passoword + text which you want to encrypt into == random text
# and if you want to see then you need random text + key + password = text you encrepted




# def write_key():
#     key = Fernet.generate_key()
#     with open('key.key', 'wb') as key_file:
#         key_file.write(key)


# to decrecpt the key
def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key


master_pwd = input("Enter your master passoward? ")
key = load_key() + master_pwd.encode()
far = Fernet(key)


def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data = (line.rstrip())
                        # rstrip function() removes the whitespace only form right end of the string
            user, passw = data.split('|')
# split create the list of element where | this charecter is stored and because
# we have only two element that's why we chose the two variable
            # "Hello|World"
            # user, passw = ["Hello","Would"] we can acess through the index
            print("User:",user,"| password:",far.encrypt(passw.encode()).decode())


def add():
    name = input("Enter the Username or account namr: ")
    add_pwd = input("Enter password: ")

    # Here we make a new file and store(append) the passowrd
    with open('password.txt','a') as f:
        # it write the name and add the passowrd and use | saperator to saperate both
        f.write(name + '|' + far.encrypt(add_pwd.encode()).decode() + '\n')
        


while True:
    mode = input("Do you want to view or add passoward (view, add). Press q to quit: ").lower()
    if mode == 'q':
        break

    if mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print("Invilid mode: ")
        continue