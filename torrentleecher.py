import libtorrent as lt
import time
import os

cwd = getcwd()

def kek():
  ses = lt.session()
  ses.listen_on(6881, 6891)
  params = {
      'save_path': cwd,
      'storage_mode': lt.storage_mode_t(2)}
  
  link = "magnet:?xt=urn:btih:86a5a0bc225655d79432751e0a1a86c955e1e123&dn=%5BSubsPlease%5D%20Majutsushi%20Orphen%20Hagure%20Tabi%20S3%20-%2002%20%281080p%29%20%5B85815371%5D.mkv&tr=http%3A%2F%2Fnyaa.tracker.wf%3A7777%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce"
  handle = lt.add_magnet_uri(ses, link, params)
  ses.start_dht()

  print ('downloading metadata...')
  while (not handle.has_metadata()):
    time.sleep(1)

  print ('got metadata, starting torrent download...')


  while (handle.status().state != lt.torrent_status.seeding):
      s = handle.status()
      state_str = ['queued', 'checking', 'downloading metadata', \
                  'downloading', 'finished', 'seeding', 'allocating']
      print(s.progress*100,s.download_rate/1000,s.upload_rate/1000,s.num_peers,state_str[s.state],s.total_download/1000000)
   
      print(f" {round(s.progress*100,2)} Complete (down: {round(s.download_rate/1000,2)} kb/s up: {round(s.upload_rate/1000,2)} kB/s peers:{s.num_peers}) {state_str[s.state]} {round(s.total_download/1000000,2)}  {s.name} ")
    
      data = f" {round(s.progress*100,2)} Complete (down: {round(s.download_rate/1000,2)} kb/s up: {round(s.upload_rate/1000,2)} kB/s peers:{s.num_peers}) {state_str[s.state]} {round(s.total_download/1000000,2)}  {s.name} "
    
      yield data
    
    #  time.sleep(5)
    
print(kek()    )
          
