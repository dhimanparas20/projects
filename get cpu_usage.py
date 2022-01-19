import os
import psutil

loadi, loads, load15 = psutil.getloadavg()
usage = (load15/os.cpu_count()) * 100
print(f"Cpu uage = {usage}%")
