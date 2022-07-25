import time

def correct_login(login: str, password: str):
    username = "admin0"
    userpass = "admin0"

    if login == username and password == userpass:
        return True

    return False

def main():
    for i in range(5):
        if i == 3:
            print("Waiting 3 secs ...")
            time.sleep(3)
        
        print("Enter login: ")
        login: str = input()

        print("Enter password: ")
        password: str = input()

        if correct_login(login=login, password=password): 
            print("Welcome ADMIN!")
            break

        print("User with such credentials was not found")


if __name__ == "__main__":
    main()