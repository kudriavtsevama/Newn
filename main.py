import sys
from cipher import caeser_encrypt, viginer_encrypt, vernam_encrypt
from freguency_analysis import hack


def error():
    print("command not found")
    print("see python3 main.py --help")
    sys.exit()


def his_file_to_str():
    file = sys.argv[3]
    with open(file) as fp:
        his_str = fp.read()  # строка
    return his_str


def caeser_do():
    if len(sys.argv) <= 3:
        error()
    what_do = sys.argv[2]
    his_str = his_file_to_str()
    if (what_do == "encrypt") or (what_do == "decrypt"): #зашифровать через ключ
        if len(sys.argv) < 5:
            error()
        key = int(sys.argv[4])
        if what_do == "encrypt":
            encrypted = caeser_encrypt(his_str, key, 1)
        else:
            encrypted = caeser_encrypt(his_str, key, -1)
        # print(encrypted)
        answer = open('answer.txt', 'w')
        answer.write(encrypted)
        print(encrypted)
    elif what_do == "hack":
        his_str = his_file_to_str()
        answer = open('answer.txt', 'w')
        ans = hack(his_str)
        answer.write(ans)
        print(ans)
    else:
        error()


def viginer_do():
    what_do = sys.argv[2]
    if len(sys.argv) <= 4:
        error()
    his_str = his_file_to_str()
    if what_do == "encrypt":  # Зашифровать через ключ
        key = sys.argv[4]
        answer = open('answer.txt', 'w')
        encrypted_text = viginer_encrypt(his_str, key, 1)
        print(encrypted_text)
        answer.write(encrypted_text)
    elif what_do == "decrypt":  # Расшифровать через ключ
        key = sys.argv[4]
        answer = open('answer.txt', 'w')
        encrypted_text = viginer_encrypt(his_str, key, -1)
        print(encrypted_text)
        answer.write(encrypted_text)
    else:
        error()


def vernam_do():
    what_do = sys.argv[2]
    if len(sys.argv) <= 4:
        error()
    his_str = his_file_to_str()
    if what_do == "encrypt":  # Зашифровать через ключ
        key = sys.argv[4]
        answer = open('answer.txt', 'w')
        encrypted_text = vernam_encrypt(his_str, key)
        print(encrypted_text)
        answer.write(encrypted_text)
    elif what_do == "decrypt":  # Расшифровать через ключ
        key = sys.argv[4]
        answer = open('answer.txt', 'w')
        encrypted_text = vernam_encrypt(his_str, key, -1)
        print(encrypted_text)
        answer.write(encrypted_text)
    else:
        error()


cipher = sys.argv[1]
if cipher == "--help" or cipher == "help":
    with open("help.txt") as fp:
        print(fp.read())
elif (len(sys.argv) < 4) or (sys.argv[2] != "hack" and len(sys.argv) != 5) or (sys.argv[2] == "hack" and len(sys.argv) != 4):
    error()
elif cipher == "caeser":
    caeser_do()
elif cipher == "viginer":
    viginer_do()
elif cipher == "vernam":
    vernam_do()
else:
    error()
