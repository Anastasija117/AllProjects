username = input("Enter username:")
password = input("Enter password:")

if username == "admin" and password == "admin123":
    print("Welcome, Administrator!You have full access to the system.")
elif username == "moderator" and password == "moderator123":
    print("Welcome, Moderator!You have access to most of the system.")
elif username == "user" and password == "user123":
    print("Welcome, Guest!You have limited access.")
else:
    print("Access denied.Incorrect username or password.")

input("End")