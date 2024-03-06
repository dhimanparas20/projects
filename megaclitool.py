from mega import Mega
from os import system, path ,getcwd ,listdir, scandir
from torrentp import TorrentDownloader
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

system("clear")

mega = Mega()
m = mega.login("<email>","<password>")

details = m.get_user()
space = m.get_storage_space(mega=True)
files = m.get_files()
cwd = getcwd()
file_auto = f"{cwd}/Auto/*"

if (path.exists('Downloads') != True) :
  system("mkdir Downloads")
  
if (path.exists('Upload') != True) :
  system("mkdir Upload && cp multidownload.txt Upload")  
  
if (path.exists('Auto') != True) :
  system("mkdir Auto")

def get_size(in_bytes):
  return in_bytes/1000000

file_count = 0
folder_count = 0
j= 1
lst =  [None]*100

'''
size= path.getsize('galaxy.jpg')
print("size = ",get_size(size))
'''

#Counts the total no of files and folders
for file in files:
  if files[file]['a'] != False and files[file]['p']!='':   
    if files[file]['t'] == 1:
      folder_count +=1
      lst[folder_count] =  files[file]['h']
    if files[file]['t'] == 0:
      file_count += 1 

def show_details():
  print("==================|DETAILS|=====================\n")
  print("User Name:     ",details['name'])
  print("Email:         ",details['email'])
  print("Phone Number:  ",details['smsv'])
  print("ID:            ",details['u'])
  print("Space Used:    ",space['used'],"MB")
  print("Space Left:    ",space['total']-space['used'],"MB")
  print("Quota:         ",space['total'],"MB")
  print("Total Folders: ",folder_count)
  print("Total files:   ",file_count)
  
def get_menue():
  input("\nPress Enter to goto Main Menue")  
      
# Diaplay main Menu
while True:
  system("clear")
  print ("------------------------------------------------")
  print ("            Choose your Choice                  ")
  print ("------------------------------------------------")
  print ("0: Show my Details")
  print ("1: Show all Files and Folders")
  print ("2: Download Mega File")
  print ("3: Upload File/Folder to Mega")
  print ("4: Find a File/Folder")
  print ("5: Create a folder")
  print ("6: Rename file/folder")
  print ("7: Import a file/folder from a Public URL")
  print ("8: Export a file/folder")
  print ("9: Download a file from Non-Mega/any url")
  print ("10:Auto download from link and upload to mega")
  print ("11:Do a speed test")
  print ("12:Refresh Details")
  print ("13:Download from torrent")
  print ("14:Upload to grive")
  print ("69: Exit")

  # User input for main menu choices.
  print ("================================================")
  inp = int(input(f"Enter your choice (number):"))
  system("clear")
  print("\n") 
  
  if inp ==0:
    show_details()
    get_menue()
   
  elif inp == 1:
    print("==================|Folders|=====================\n")
    for file in files:
      if files[file]['a'] != False and files[file]['p']!='' and files[file]['t'] == 1  : 
        print(f"{j}.",files[file]['a']['n']) 
        j +=1

    print("\n==================|Files|=====================\n")
    j = 1
    for file in files:    
      if files[file]['a'] != False and files[file]['p']!='' and files[file]['t'] == 0  : 
        print(f"{j}.",files[file]['a']['n']) 
        j +=1  
    get_menue()      
 
  elif inp ==2:
    inp = int(input(f"1. By file name.\n2. By Url.\n--> "))
    name = input("Enter the file name/URL to download: ")
    if inp ==1: 
      try:
        file = m.find(name)
        m.download(file,f"{cwd}/Downloads")
      except:
        print("ERROR: No such file exists")    
        
    elif inp ==2:
      try:
        m.download_url(name,f"{cwd}/Downloads")
      except:
        print("ERROR: No such Link exists")  
    get_menue()
  
  elif inp ==3:
    name = input("Enter file/folder name to Upload: ") 
    size= path.getsize(f'{cwd}/Upload/{name}')
    if size > space['total']-space['used']:
      print("File size greater than available Space on Cloud")
    else:
      #folder = m.find('my_mega_folder')
      m.upload(f"{cwd}/Upload/{name}") 
    
    get_menue()
 
  elif inp == 4:
    name = input("Enter file/folder name to find: ") 
    folder = m.find(name,exclude_deleted=True)
    if folder ==  None:
      print("No Such File Found")  
    else :
      print("Found: ",folder[1]['a']['n'])
      try:
        print("File Size:  ",get_size(folder[1]['s']),"MB")
      except:
        pass
    get_menue()
    
  elif inp == 5:
    name = input("Enter Name of folder to create: ")
    m.create_folder(name)
    get_menue()   
  
  elif inp == 6:
    name_old = input("Enter the original name of file to rename: ")  
    name_new = input("Enter the new name of file: ")
    file = m.find(name_old)
    m.rename(file, name_new)
    get_menue()
    
  elif inp == 7:  
    url = input("Enter File URL: ")
    m.import_public_url(url)
    get_menue()
    
  elif inp == 8:   
    name = input("Enter Name of file/folder to export: ")
    public_exported_web_link = m.export(name)
    print(public_exported_web_link)
    get_menue()
    
  elif inp == 9:  
    url = input("Enter URL of the file: ")
    system(f"cd Upload && wget -q --show-progress  {url}")
    #system(f"cd Auto && curl -O  {url}")
    #system(f"cd Upload && wget -i multidownload.txt -q --show-progress")
    
  elif inp == 10:
    url = input("Enter URL of the file: ")
    try:
      system(f"cd Auto && wget -q --show-progress  {url}")
      #system(f"cd Auto && curl -O  {url}")
      #system(f"cd Upload && wget -i multidownload.txt -q --show-progress")    
      size= path.getsize(f'{cwd}/Auto/')
      if size > space['total']-space['used']:
        print("File size greater than available Space on Cloud")
      else:
        #folder = m.find('my_mega_folder')
        name = listdir(f"{cwd}/Auto/")
        try:
          if name[1] != None:
            system(f"cd Auto && rm -rf {name[1]}")
        except:
          pass    
        m.upload(f"{cwd}/Auto/{name[0]}")
        system("cd Auto && rm -rf *")
    except:  
      pass
    get_menue()
    
  elif inp == 11:
    system("sudo pip install speedtest-cli")  
    system("speedtest --single")
    #system("speedtest --simple")
    get_menue()
    
  elif inp == 12:  
    file_count = 0
    folder_count = 0
    space = m.get_storage_space(mega=True)
    files = m.get_files()
    for file in files:
      if files[file]['a'] != False and files[file]['p']!='':   
        if files[file]['t'] == 1:
          folder_count +=1
          lst[folder_count] =  files[file]['h']
        if files[file]['t'] == 0:
          file_count += 1

    get_menue()
  
  elif inp ==69:
    exit()
 
