import psutil

#number of cores
print("Physical cores:",psutil.cpu_count(logical=False))
print("Total cores:",psutil.cpu_count(logical=True))

#CPU frequencies
freq = psutil.cpu_freq()
print(f"Maximum Frequency: {freq.max:.2f}Mhz")
print(f"Minimum Frequency: {freq.min:.2f}Mhz")
print(f"Current Frequency: {freq.current:.2f}Mhz")

#CPU Usage
print("CPU usage per core: ")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")