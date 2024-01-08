import speedtest

st = speedtest.Speedtest()

#st.get_servers()  # Get list of servers
#st.get_best_server()  # Find best server

st.download(threads=None)  # Download speed test with default threads
st.upload(threads=None)  # Upload speed test with default threads

download_speed = st.results.download / 10**6  # Convert to Mbps
upload_speed = st.results.upload / 10**6  # Convert to Mbps

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
