1. create repository in github.
2. create an ML folder in your D drive.
3. open anaconda and enter in to that D drive folder using CD then write code . to open VS Code.
4. Create new terminal(powershell or command prompt) in VS code to perofrm various tasks:
 a. create environment venv using conda create -p venv python==3.8 -y then activate this venv environment.
 b. Now We need to link the repository created in github to sync with our vs code to commit all our code using below cmmands in vs code:
    	git init
	git add README.md
	git commit -m "first commit"
	git branch -M main
	git remote add origin https://github.com/vishai1990/ML_Project1.git
	git push -u origin main
	git pull to update in vs code as i have created .ignore file manually in github to not commit any changes that i do not want to in the githuub repository
5. Now create, setup.py(creates ml application in packages) and requirements.txt(to write all the packages that i wnat to install) in ML project folder in VS code 
6. Create src folder s well and __init__.py file in it as find_package() in setup.py tries to find the package inside the src folder
7. 