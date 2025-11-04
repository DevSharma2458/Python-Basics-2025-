# Install  pandas, moviepy, virtualenv by using "pip install pandas or moviepy or virtualenv" command on your terminal after that 
# apply virtual env by using this command "python -m venv env1"
# then activate venv by ".\env1\Scripts\activate.ps1 " --> Use Tab after writing env1 then Script in terminal
# Now install pandas again in venv
# and pip install requests
# You can install particular version package for an example "pip install numpy==1.20.0" to install a specific version
#  Install scipy by pip install scipy


# If you want to check the list of packages install then use this command "pip list" to check the list of packages installed 

# You can also upgrade a particular package by running this command "pip install --upgrade requests(here we are upgrading requests package)"

# you can uninstall a package by using this command "pip uninstall requests(here we removed requests package)"

# Generating a requirements.txt file which contains all the packages your project depends on, This makes it easy to recretae the env on another devide

# First create a file named requirements.txt and then fill in the names of packages that you want to install in like pandas, requests, scipy, moviepy and etc 

# Now you can cretae requirements,txt by using "pip freeze > requirements.txt"
# This will create a requirements.txt file and bydefault will include all the packages being used by your project

# If you want to install requirements.txt use this command  "pip install -r .\requirements.txt" this will scan all the packages inside requirements.txt and will install it one by one. You can check this command by creating another venv named env2 and then in that venv you can use this command and take all the packages from env1 to env2

# To check the packages with version number you can use "pip freeze"

# If you want to deactive the virtual env then type the command "deactivate" this will deactivate this virtual env
