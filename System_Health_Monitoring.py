import psutil
import logging

# Set alert thresholds for CPU, Memory, Disk usage and number of processes
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80
PROCESS_THRESHOLD = 200

# Configure logging to write warnings to a file
logging.basicConfig(filename="system_health.log", level=logging.WARNING)

# Check CPU usage over a 1-second interval
cpu = psutil.cpu_percent(interval=1)
print("CPU Usage:", cpu, "%")
if cpu > CPU_THRESHOLD:
    message = "Alert: CPU usage is above 80%"
    print(message)
    logging.warning(message)

# Check Memory usage of the system  
memory = psutil.virtual_memory().percent
print("Memory Usage:", memory, "%")
if memory > MEMORY_THRESHOLD:
    message = "Alert: Memory usage is above 80%"
    print(message)
    logging.warning(message)

# Check Disk usage
disk = psutil.disk_usage('/').percent
print("Disk Usage:", disk, "%")
if disk > DISK_THRESHOLD:
    message = "Alert: Disk usage is above 80%"
    print(message)
    logging.warning(message)

# Check number of running processes in the system
process_count = len(psutil.pids())
print("Running Processes:", process_count)
if process_count > PROCESS_THRESHOLD:
    message = "Alert: Too many processes running"
    print(message)
    logging.warning(message)
