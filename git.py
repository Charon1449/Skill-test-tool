from github import Github

# First create a Github instance:


# or using an access token
g = Github("632ae7ed42bf8b7d4cd270f8ffb4ee1b83ed7eb7")



# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)