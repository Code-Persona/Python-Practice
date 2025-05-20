# Request User input 
# Check length of the input
# Give condition that if n > 12 that we hit an error  
# Check if the input has spaces
# Check if the input has has digits

username = input("Enter your username: ")
# Check length of the input

if len(username) > 12:
    print("Error: Username must be less than 12 characters.")
# Check if the input has spaces
elif not username.find(" ") == -1: #if result is -1 then there are no spaces
    print("Error: Username must not contain spaces.")
elif not username.isalpha():
    print("Error: Username must not contain digits.")
else:
    print(f"Welcome {username}")