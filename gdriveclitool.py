from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from os import system, path ,getcwd ,listdir, scandir
from torrentp import TorrentDownloader
system("clear")

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

cwd = getcwd()

# Edit This Only
team_drive_id = '0AP6HKB1xn_xdUk9PVA'
#parent_folder_id = ''

if (path.exists('Files') != True) :
  system("mkdir Files")
if (path.exists('Auto') != True) :
  system("mkdir Auto")

# To Upload Files to TeamDrive
def upload(filename,path):
  f = drive.CreateFile({
    'title': filename,
    'parents': [{
        'kind': 'drive#fileLink',
        'teamDriveId': team_drive_id,
        'id': team_drive_id
    }]
  })
  f.SetContentFile(path)
  f.Upload(param={'supportsTeamDrives': True})

def barr(no):
  if no <= 10:
    bar = "■□□□□□□□□□"
  elif no <=20:
    bar = "■■□□□□□□□□"
  elif no <=30:
    bar = "■■■□□□□□□□"
  elif no <=40:
    bar = "■■■■□□□□□□"
  elif no <=50:
    bar = "■■■■■□□□□□"
  elif no <=60:
    bar = "■■■■■■□□□□"
  elif no <=70:
    bar = "■■■■■■■□□□"
  elif no <=80:
    bar = "■■■■■■■■□□"
  elif no <=90:
    bar = "■■■■■■■■■□"
  elif no <=105:
    bar = "■■■■■■■■■■"
  return(bar)  

a,tm,min,hr,sec = 0,0,0,0,0
def bart(current,total,self):
  system("clear")
  global a,tm,min,hr,sec
  current =round(current*0.000001,2)
  total =  round(total*0.000001,2)
  percy = (current/total)*100
  print(f"Downloaded {round((current/total)*100,2)} %")
  print(f"Downloaded {current}MB/{round(total,2)}MB")
  percy = round((current/total)*100,2)
  print(barr(percy))
  for i in range (0,int(total),1):
    if current == i-1:
      a = round(time.time(),5)
    if  current == i :
      b= round(time.time(),5)
    tm = round(b-a,5)
    print("tm-------------------------->",tm," s")
    if tm <= 0.011:
      tm = 0.15
                
    speed = 1/tm
    print("speed: ",round(1/tm,2),"MB/s")
    ac = total/speed
    bc = round((total-current)/(1/tm),2)
    msg = f"{barr(percy)} {percy}% \n{current}MB/{round(total,2)}MB\nSpeed: {round(1/tm,2)}"   
    edit_message(chat_id,m_id+1,msg)
    if bc >= 60 :
      min = int(bc/60)
      if min >=60:
        hr = int(min/60)
        min = round(min-(60*hr),2)
        print(f"time remaining: {hr}H {min}M")
      elif min <60 and bc >=60:
        sec = round(bc-(min*60),2)
      print(f"time remaining: {min} min {sec}s")
    else:
      print(f"time remaining: {bc}s")


def get_menue():
  input("\nPress Enter to goto Main Menue")  
      

# Diaplay main Menu
while True:
  system("clear")
  print ("------------------------------------------------")
  print ("            Choose your Choice                  ")
  print ("------------------------------------------------")
  print ("0: Generate Credentials.json file")
  print ("1: Upload a file")
  print ("2: Download a file from url/Torrent")
  print ("3: Auto download from link and upload to Gdrive")
  print ("4: Auto download from link and upload to Gdrive as zip")
  print ("5: Do a speed test")
  print ("6: Search A file")
  print ("69: Exit")

  # User input for main menu choices.
  print ("================================================")
  inp = int(input(f"Enter your choice (number):"))
  system("clear")
  print("\n") 
  
  if inp ==0:
    try:
      gauth.LocalWebserverAuth()
    except:
      print("No client_secrets.json file.\nPlease get it by following 'https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf'")  
    get_menue()
   
  elif inp == 1:
    try:
      obj = scandir(f"{cwd}/Files")
      print("=============Available Files===============")
      for entry in obj:
        if entry.is_dir() or entry.is_file():
          print(entry.name)
      print("===========================================")    
      name = input("Enter file/folder name to Upload.\n(file should be inside Upload Folder) --> ") 
      print("-----------------Uploading-----------------\n")
      upload(name,f"{cwd}/Files/{name}") 
      print("\n--------------Uploading Done---------------")
      print(f"URL: https://luffy.mst-uploads.workers.dev/0:/{name}?a=view")
    except:
      print("Uploading error")  
    get_menue()      
    
  elif inp == 2:  
    url = input("Enter URL of the file: ")
    try:
      if "magnet" in url :
        print("---------------Torrent detected-----------------------")
        print("\n")
        torrent_file = TorrentDownloader(url, f"{cwd}/Files")
        torrent_file.start_download()
      else:  
        loc = f"{cwd}/Files"
        download(url,loc,bar=bart)
        system(f"cd Files && wget -q --show-progress  {url}")
        #system(f"cd Auto && curl -O  {url}")
        #system(f"cd Upload && wget -i multidownload.txt -q --show-progress") 
      print("-----------------Download Complete--------------------")   
    except:
      print("Download error")  
    get_menue() 
    
  elif inp == 3:
    url = input("Enter torrent/file URL: ")
    try:
      print("--------------Downloadin--------------------")
      if "magnet" in url :
        print("---------------Torrent detected-----------------------")
        print("\n")
        torrent_file = TorrentDownloader(url, f"{cwd}/Auto")
        torrent_file.start_download()
      else:  
        system(f"cd Auto && wget -q --show-progress  {url}")
        #system(f"cd Auto && curl -O  {url}")
        #system(f"cd Upload && wget -i multidownload.txt -q --show-progress")
      name = listdir(f"{cwd}/Auto/")
      try:
        if name[1] != None:
          system(f"cd Auto && rm -rf {name[1]}")
      except:
        pass   
      print("--------------Uploading--------------------") 
      upload(name[0],f"{cwd}/Auto/{name[0]}")
      print(f"URL: https://luffy.mst-uploads.workers.dev/0:/{name[0]}?a=view")
      system("cd Auto && rm -rf *")
    except:  
      print("------------error occured-----------------")
    get_menue()  
    
  elif inp == 4:
    url = input("Enter torrent/file URL: ")
#    try:
    print("--------------Downloadin--------------------")
    if "magnet" in url :
      print("---------------Torrent detected-----------------------")
      print("\n")
      torrent_file = TorrentDownloader(url, f"{cwd}/Auto")
      torrent_file.start_download()
    else:  
      system(f"cd Auto && wget -q --show-progress  {url}")
      #system(f"cd Auto && curl -O  {url}")
      #system(f"cd Upload && wget -i multidownload.txt -q --show-progress")  
    name = listdir(f"{cwd}/Auto/")
    n = name[0]
    n = n.replace(' ', '_')
    print(n)
    system(f"cd Auto && mv '{name[0]}' {n} && rm -rf {name[0]}")  
    if path.isfile(f"{cwd}/Auto/{n}") == True:
      cut = n.split(".")[-1]
      spl = n.replace(f".{cut}", '')
    else:
      print("------------------nothing to split----------------------")
      spl = n
    system(f"cd Auto && zip -r zipped_file {n} && mv zipped_file.zip {spl}.zip")
    new_name = f"{spl}.zip"
    try:
      if name[1] != None:
        system(f"cd Auto && rm -rf {name[1]}")
    except:
      pass   
    print("--------------Uploading--------------------") 
    upload(new_name,f"{cwd}/Auto/{new_name}")
    print(f"URL: https://luffy.mst-uploads.workers.dev/0:/{new_name}?a=view")
    system("cd Auto && rm -rf *")
#    except:  
#      print("------------error occured-----------------")
    get_menue()
    
  elif inp == 5:
    #system("sudo pip install speedtest-cli")  
    system("speedtest --single")
    #system("speedtest --simple")
    get_menue()
    
  elif inp == 6:
    filename = input("Enter File Name: ")
    #mimetype = "jpeg"
    query = {'q': f"title = '{filename}'"}
    #query = {'q': f"title = '{filename}' and mimeType='{mimetype}'"}
    # Get list of files that match against the query
    files = drive.ListFile(query).GetList()  
    print(files)
    print("--------------------------------------------------------------------------")
    print(files[0]['fileExtension'])
    print(files[0]['mimeType'])
    #print(files[]['mimeType'])
    print(len(files))
    input("ok ?")
  elif inp ==69:
    exit()
