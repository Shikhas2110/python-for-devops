import psutil

def system_health():
    cpu_threshold = int(input("Enter CPU threshold: "))   # CPU threshold entry by user
    mem_threshold = int(input("Enter Memory threshold: ")) # Memory threshold entry by user
    disk_threshold = int(input("Enter Disk threshold: "))  # Disk threshold entry by user

    # CPU usage
    current_cpu = psutil.cpu_percent(interval=2)
    print("Current CPU usage is", current_cpu)

    # Memory usage
    current_mem = psutil.virtual_memory().percent
    print("Current Memory usage is", current_mem)

    # Disk usage
    current_disk = psutil.disk_usage("/").percent
    print("Current Disk usage is", current_disk)

    # CPU check
    if current_cpu > cpu_threshold:
        print("Sent alert email: CPU usage high")
    else:
        print("CPU is normal")

    # Memory check
    if current_mem > mem_threshold:
        print("Sent alert email: Memory usage high")
    else:
        print("Memory is normal")

    # Disk check
    if current_disk > disk_threshold:
        print("Sent alert email: Disk usage high")
    else:
        print("Disk usage is normal")

system_health()