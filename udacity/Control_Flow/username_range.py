usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for user in range(len(usernames)):
    usernames[user] = usernames[user].lower().replace(" ","-")

print(usernames)