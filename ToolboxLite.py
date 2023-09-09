import time
import phonenumbers
import geocoder
import folium


name = open("Name.txt", 'r')
password = open("Password.txt", 'r')
passans1 = password.read()

print("Hello,please put your password")
passans = input("Here you put the password: ")


if passans == passans1:
   print("Loading " + "*____")
   time.sleep(1)
   print("Loading " + "**___")
   time.sleep(1)
   print("Loading " + "***__")
   time.sleep(1)
   print("Loading " + "****_")
   time.sleep(1)
   print("Loading complete")
  
   print("ＴｏｏｌｂｏｘＬｉｔｅ")
   print("by mr.melu")
   print("[1]Ip locator")
   print("[2]Phone Locator")
   print("[3]InstaFinder")
   print("[4]Info about an website")
  
   ans = input("Choose an option: ")
  
   if ans == "1":
     n = input("What is the ip: ")
     print("The ip is:", n)

     g = geocoder.ip(n)

     myAddress = g.latlng
     print(myAddress)
     
   elif ans == "2":
         from phonenumbers import geocoder

         from phonenumbers import carrier
         
         
         number = input("Enter the number ")

         
         ch_number = phonenumbers.parse(number, "CH")
         a = print(geocoder.description_for_number(ch_number, "en"))
         print(a)
         

         from phonenumbers import carrier
         service_number = phonenumbers.parse(number, "RO")
         b = print(carrier.name_for_number(service_number, "en"))
         print(b)
         
         
         
   if ans == "3": 
         insta = instaloader.Instaloader()

         print("INSTA FINDER by melu")
         username = input("Enter the username: ")

         profile = instaloader.Profile.from_username(insta.context, username)
         print("Username: ", profile.username)
         print("Number of posts: ", profile.mediacount)
         print("Followers: ", profile.followers)
         print("Bio: ", profile.biography)
         print("Link: ", "https://www.instagram.com/" + username + "/")
         
else:
   exit()