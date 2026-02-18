# myproject.py
# A simple Python app example

def greet_user(name):
    return f"Hello, {name}! Welcome to my Python app."

def main():
    print("=== My Simple Python App ===")
    user_name = input("Enter your name: ")
    message = greet_user(user_name)
    print(message)

if __name__ == "__main__":
    main()
