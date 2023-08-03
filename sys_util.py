import psutil
import logging
import time
import sys

# Configure the logging module to log data to a file
logging.basicConfig(filename='system_usage_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_disk_space():
    disk_usage = psutil.disk_usage('/')
    total_space_mb = disk_usage.total / (1024 * 1024)  # Convert bytes to MB
    used_space_mb = disk_usage.used / (1024 * 1024)
    available_space_mb = disk_usage.free / (1024 * 1024)
    return total_space_mb, used_space_mb, available_space_mb

def get_system_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    total_ram_mb = ram.total / (1024 * 1024)  # Convert bytes to MB
    used_ram_mb = ram.used / (1024 * 1024)
    return cpu_usage, total_ram_mb, used_ram_mb

def log_disk_and_system_usage():
    try:
        while True:
            total_mb, used_mb, available_mb = get_disk_space()
            cpu_usage, total_ram_mb, used_ram_mb = get_system_usage()
            disk_usage_percentage = (used_mb / total_mb) * 100
            ram_usage_percentage = (used_ram_mb / total_ram_mb) * 100

            log_message = (
                f"Disk Space: Total: {total_mb:.2f} MB | Used: {used_mb:.2f} MB | Available: {available_mb:.2f} MB | Usage: {disk_usage_percentage:.2f}%\n"
                f"CPU Usage: {cpu_usage:.2f}%\n"
                f"RAM: Total: {total_ram_mb:.2f} MB | Used: {used_ram_mb:.2f} MB | Usage: {ram_usage_percentage:.2f}%"
            )

            print(log_message)
            logging.info(log_message)
            time.sleep(5)  # Log data every 30 seconds
    except KeyboardInterrupt:
        print("\nExiting the program...")
        sys.exit(0)

def main():
    log_disk_and_system_usage()

if __name__ == "__main__":
    main()
