import time
import libtorrent as lt
import os
from pathlib import Path

magnet_link = "magnet:?xt=urn:btih:8015697502D76D4AC4744F9F89BC4980460C3F5D&dn=[1337x.HashHackers.Com]Bag.of.Lies.2024.1080p.BluRay.DDP5.1.x265.10bit-GalaxyRG265&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.birkenwald.de%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentor.org%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.dler.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fuploads.gamecoast.net%3A6969%2Fannounce&tr=https%3A%2F%2Ftracker.foreverpirates.co%3A443%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"

print("00000000000000000000000000000000000")
download_dir = Path("downloadss")
download_dir.mkdir(parents=True, exist_ok=True)

# Create the session settings
settings = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'announce_to_all_tiers': True,
    'enable_outgoing_utp': True,
    'enable_incoming_utp': True
}
# Create the session for downloading with the settings
ses = lt.session(settings)
print("-------------------------------------------------")

# Add the magnet link to the session
handle = lt.add_magnet_uri(ses, magnet_link, {"save_path": "downloads"})
print("====================================================")
# Start downloading the torrent
ses.resume()
print("77777777777777777777777777777")

# Loop until the download is completed
while not handle.has_metadata():
    pass

# Get the total size and file name of the torrent files
torrent_info = handle.get_torrent_info()
total_bytes = torrent_info.total_size()
file_name = torrent_info.name()
file_type = '.magnet'

# Create a torrent handle to track progress
tor_handle = ses.find_torrent(handle.info_hash())
tor_handle.set_max_connections(200)
tor_handle.set_max_uploads(-1)

#Create sttart time
start_time = time.time()

# Loop to update the download progress
while not tor_handle.is_seed():
    s = tor_handle.status()

    # Update download progress
    downloaded_bytes = s.total_done

    # Calculate download speed and time remaining
    elapsed_time = time.time() - start_time
    download_speed = (f"{(s.download_rate / 1024)/1024:.2f} MB/s")  # in KB/s
    progress = (downloaded_bytes / total_bytes) * 100
    print("\n================================")
    print(file_name)
    print(file_type)
    print(torrent_info)
    print(total_bytes/1024/1024)
    print(downloaded_bytes)
    print(progress)
    print(download_speed)
