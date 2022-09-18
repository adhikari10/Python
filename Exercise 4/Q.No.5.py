print("Login:")
t = 1
while t <= 5:
    username = input("enter username: ")
    password = input("enter password: ")
    t += 1
    if username != 'python' and password != 'rules':
        print("incorrect username or password")
        continue
    else:
        print("welcome")
        break
else:
    print("access denied")




