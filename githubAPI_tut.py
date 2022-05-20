from github import Github


#Open the Token File for the user token
#MAKE SURE YOU HAVE YOUR TOKEN GENERATED FROM GITHUB AND SAVE IT AS A FILE IN THE SAME DIRECTORY
with open("access_token", 'r') as tokenFile:
    tokenText = tokenFile.read()

#create user login
user_login = Github(str(tokenText))

print(user_login.get_user("cloudtechhills"))
ozurumba = user_login.get_repo("cloudtechhills/basic_Python_Programs")
print(f"StarGazerCount: {ozurumba.stargazers_count}")
print()

print("*"*50)
print()

   
    
try:
    
    for repo in user_login.get_user().get_repos():
        print(repo.name)
        
except KeyboardInterrupt:
    
    print("\nLooping Stopped...")