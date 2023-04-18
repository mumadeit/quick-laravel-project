import os

# ANSI escape sequences for font colors
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
END = '\033[0m'

# define creator name
creator_name = "Mu Made It"

# print a message to give credit to creator
print(f"This script was created by {GREEN}{creator_name}{END} ⚡️.")
print(f"{BLUE}This will install the latest Laravel version.{END}")

# prompt user to start installing Laravel project
input(f"{RED}Press Enter to start installing the Laravel project...{END}")

# get project name from user
project_name = input("Enter project name (NO SPACES): ")

# create new Laravel project with specified name
os.system(f"composer create-project laravel/laravel {project_name}")

# park and link the new project with Valet
os.chdir(f"{project_name}")
os.system("valet park")
os.system("valet link")
# URL after installation
project_url = f"http://{project_name}.test"
print(f"{GREEN}Laravel installed successfully!{END} Project URL: {BLUE}{project_url}{END}")
