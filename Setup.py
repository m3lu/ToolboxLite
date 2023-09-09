import sys 
import subprocess

print("Hello and welcome to the ToolboxLite' setup")
name = input("Here you need to put your name: ")
namefile = open("Name.txt", 'w')
password = input("Here you'll put the password you want to use: ")
namepassword = open("Password.txt", 'w')

print("Please wait")
print("We are installing the required packages")

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'folium'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'geocoder'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'instaloader'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])