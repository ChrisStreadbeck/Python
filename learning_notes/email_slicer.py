email = input("What is your email address?: ").strip()
user = email[:email.index("@")]
domain = email[email.index("@") + 1:]

output = "your username is {} and your domain name is {}".format(user, domain)

print(output)