current_users=["Timmy","Jimmy", "Slade", "Frosty", "Jamie"]
lower_users=[]
for user in current_users:
    lower_users.append(user.lower())
    

new_users=["Franky","Levi", "Jack", "Frosty", "Jamie"]

if new_users == "Franky":
    print("Username available")
if new_users == "Levi":
    print("Username available")
if new_users == "Jack":
    print("Username available")
if new_users == "Frosty":
    print("Username unavailable, try again.")
if new_users == "Jamie":
    print("Username unavailable, try again.")