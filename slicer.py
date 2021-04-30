# Get user e-mail address

email = input("What is your e-mail address?: ").strip()

# Slice out user name

user = email[:email.index("@")]

# Slice out domain name

domain = email[email.index("@") + 1 :]

# Format message
output = "Your username is {} and your domain name is {}.".format(user, domain)

# Display output message

print(output)