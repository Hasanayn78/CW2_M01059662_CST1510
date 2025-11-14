
import bcrypt

# --- File name for storing users ---
USER_FILE = "users.txt"

# --- Function to hash password ---
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

# --- Function to verify password ---
def verify_password(plain_text_password, hashed_password):
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

# --- Save user to file ---
def save_user(username, hashed_password):
    with open(USER_FILE, "a") as file:
        file.write(f"{username},{hashed_password.decode('utf-8')}\n")

# --- Check if user exists ---
def user_exists(username):
    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                saved_username, _ = line.strip().split(",", 1)
                if saved_username == username:
                    return True
    except FileNotFoundError:
        pass
    return False

# --- Register a new user ---
def register_user():
    username = input("Enter a new username: ")
    if user_exists(username):
        print(" That username already exists.")
        return

    password = input("Enter a new password: ")
    hashed_password = hash_password(password)
    save_user(username, hashed_password)
    print(" User registered successfully!")

# --- Login an existing user ---
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                saved_username, saved_hashed = line.strip().split(",", 1)
                if saved_username == username:
                    if verify_password(password, saved_hashed.encode('utf-8')):
                        print(" Login successful!")
                        return
                    else:
                        print(" Wrong password.")
                        return
        print(" Username not found.")
    except FileNotFoundError:
        print(" No users found yet. Register first!")

# --- Main program ---
def main():
    while True:
        print("\n--- LOGIN SYSTEM ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")

if __name__ == "__main__":
    main()



