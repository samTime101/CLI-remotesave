# FEB 4 : updated the /write , sent JSON data instead


# CLI for remote save
# Author : SAMIP REGMI
# Jan 29 2:18 PM

# html escape garna , for codes
import requests
import html
# for hidden pass input
from getpass import getpass

#address = "http://127.0.0.1:5000"
address = "https://samip.pythonanywhere.com"
def fetch_data(endpoint):
    url = f"{address}/space/{endpoint}"
    response = requests.get(url)
    contents = response.json()
#    print(contents)
    if 'folder' in contents:
        print(contents['folder'])
        user_input()
    elif 'file' in contents:
        print(contents['file'])
        main()
# TODO : TO FIX THIS ELSE BLOCK
# BEING INVOKED WHEN I DOUBLE SPACE AND 5
#    else:
#        print("Error from fetch")
#        return


def user_input():
    user = input("<double space to exit> <ENTER to see spaces> path: ")
    if '  ' in user:
        main()
    fetch_data(user)

def create_space():
    try:
        space_name = input("Enter space name: ")
        space_password = getpass("Enter space password: ")
        if ' ' in space_name or not space_name or not space_password:
            raise Exception("ERROR: whitespace or no input at space name or pass")
        url = f"{address}/create/{space_name}"
        headers = {"Content-Type": "text/plain"}
        response = requests.post(url, headers=headers, data=space_password)
        print(response)
        main()
    except Exception as e:
        print(e)
        return

def create_subspace():
    try:
        space_name = input("Enter path: ")
        target = input("Enter subspace name: ")
        space_password = getpass("Enter space password: ")
        if ' ' in space_name or not space_name or not space_password or ' ' in target or not target:
            raise Exception("ERROR")
        url = f"{address}/sub/{space_name}/{target}"
        headers = {"Content-Type": "text/plain"}
        response = requests.post(url, headers=headers, data=space_password)
        print(response)
        main()
    except Exception as e:
        print(e)
        return


def write_content():
    try:
        space_name = input("Enter path: ")
        #target = input("Enter file name: ")
        while True:
            try:
                user_choice = int(input("Upload(1) or write(2)?: "))
                target = input("Enter file name: ")
                if user_choice == 1:
                    with open(target,'r') as file:
                        content = file.read()
                        break
                elif user_choice == 2:
                    content = input("Enter your contetn:")
                    break
                else:
                    print("error")
                    return
            except Exception as e:
                print(e)
        space_password = getpass("Enter space password: ")
        try:
            user_escape = input("'y' to escape , Enter to default: ").lower()
            if user_escape == 'y':
                content = html.escape(content)
        except Exception as e:
            print(e)
            return
        if ' ' in space_name or not space_name or not space_password or ' ' in target or not target:
            raise Exception("ERROR")
        url = f"{address}/write/{space_name}/{target}"
        headers = {"Content-Type": "application/json"}
        json_data = {"password":space_password,"content":content}
        response = requests.post(url, headers=headers, json=json_data)
        print(response)
        main()
    except Exception as e:
        print(e)
        return

def edit_content():
    try:
        space_name = input("Enter path: ")
        target = input("Enter file name you wanna edit: ")
        file_content_to_be_sent = input("Enter filename whose content u wanna send: ")
        try:
            with open(file_content_to_be_sent,"r") as file:
                content = file.read()
        except Exception as e:
            print(e)
            return
        space_password = getpass("Enter admin password: ")
        try:
            user_escape = input("'y' to escape , Enter to default: ").lower()
            if user_escape == 'y':
                content = html.escape(content)
        except Exception as e:
            print(e)
            return
        if ' ' in space_name or not space_name or not space_password or ' ' in target or not target:
            raise Exception("ERROR")
        url = f"{address}/edit/{space_name}/{target}"
        headers = {"Content-Type": "application/json"}
        json_data = {"password":space_password,"new_content":content}
        response = requests.post(url, headers=headers, json=json_data)
        print(response)
        main()
    except Exception as e:
        print(e)
        return
def main():
    print("FEB 4:\n")
    user_choice = int(input('1 for fetching data\n2 for creating space\n3 for creating subspace\n4 write content\n5 edit content(via upload)\n6 exit: '))
    try:
        if user_choice == 1:
            user_input()
        elif user_choice == 2:
            create_space()
        elif user_choice == 3:
            create_subspace()
        elif user_choice == 4:
            write_content()
        elif user_choice == 5:
            edit_content()
        elif user_choice == 6:
            print('EXIT REQUESTED\nSHAREVER\nAUTHOR:SAMIP REGMI\nCLI FOR SHAREVER PYTHON\n')
            return
        else:
            print("ERROR")
            return
    except Exception as e:
        print(e)
main()
