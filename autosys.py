from modules import monitor, cleanup, notifier, package_manager, scheduler, security

def main():
    print("AutoSys Toolkit Starting...")
    print(f"CPU Usage: {monitor.get_cpu_usage()}%")
    print(f"Memory Usage: {monitor.get_memory_usage()}%")
    print(f"Disk Usage: {monitor.get_disk_usage()}%")

    cleanup.clean_temp_files()
    package_manager.update_packages()
    security.check_open_ports()

if __name__ == "__main__":
    main()
