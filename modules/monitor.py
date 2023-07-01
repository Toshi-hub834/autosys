# modules/monitor.py
# This module uses the psutil library to fetch real-time system metrics.

import psutil # Import the psutil library for system monitoring
import datetime # Used for timestamping data

def get_cpu_usage():
    """
    Fetches the current CPU utilization percentage.
    Returns a dictionary with 'percent' and 'unit'.
    """
    # psutil.cpu_percent(interval=1) blocks for 1 second to calculate
    # the percentage over that interval. We call it without an interval
    # here for a non-blocking call, assuming it's called frequently enough
    # by the web application to get meaningful updates.
    cpu_percent = psutil.cpu_percent(interval=None)
    return {"percent": cpu_percent, "unit": "%"}

def get_memory_usage():
    """
    Fetches the current memory utilization.
    Returns a dictionary with 'total', 'used', 'free', 'percent', and 'unit'.
    Values are in GB for easier readability.
    """
    memory = psutil.virtual_memory()
    # Convert bytes to gigabytes for better readability
    total_gb = round(memory.total / (1024**3), 2)
    used_gb = round(memory.used / (1024**3), 2)
    free_gb = round(memory.free / (1024**3), 2)

    return {
        "total": total_gb,
        "used": used_gb,
        "free": free_gb,
        "percent": memory.percent,
        "unit": "GB"
    }

def get_disk_usage(path='/'):
    """
    Fetches the disk utilization for a given path (defaulting to root '/').
    Returns a dictionary with 'total', 'used', 'free', 'percent', and 'unit'.
    Values are in GB.
    """
    try:
        disk = psutil.disk_usage(path)
        # Convert bytes to gigabytes
        total_gb = round(disk.total / (1024**3), 2)
        used_gb = round(disk.used / (1024**3), 2)
        free_gb = round(disk.free / (1024**3), 2)
        return {
            "total": total_gb,
            "used": used_gb,
            "free": free_gb,
            "percent": disk.percent,
            "unit": "GB",
            "path": path
        }
    except Exception as e:
        return {"error": f"Could not get disk usage for {path}: {e}", "path": path}

# Store previous network counters to calculate delta
_last_net_io_counters = psutil.net_io_counters()
_last_net_io_time = datetime.datetime.now()

def get_network_io():
    """
    Fetches network I/O statistics (bytes sent and received).
    Calculates the rate (bytes/second) since the last call.
    Returns a dictionary with 'bytes_sent', 'bytes_recv', 'sent_rate_mbps',
    'recv_rate_mbps', and 'timestamp'.
    """
    global _last_net_io_counters, _last_net_io_time

    current_net_io = psutil.net_io_counters()
    current_time = datetime.datetime.now()

    time_diff_seconds = (current_time - _last_net_io_time).total_seconds()

    bytes_sent_delta = current_net_io.bytes_sent - _last_net_io_counters.bytes_sent
    bytes_recv_delta = current_net_io.bytes_recv - _last_net_io_counters.bytes_recv

    # Calculate rates in MB/s
    sent_rate_mbps = round((bytes_sent_delta / time_diff_seconds) / (1024 * 1024), 2) if time_diff_seconds > 0 else 0
    recv_rate_mbps = round((bytes_recv_delta / time_diff_seconds) / (1024 * 1024), 2) if time_diff_seconds > 0 else 0

    _last_net_io_counters = current_net_io
    _last_net_io_time = current_time

    return {
        "bytes_sent": current_net_io.bytes_sent,
        "bytes_recv": current_net_io.bytes_recv,
        "sent_rate_mbps": sent_rate_mbps,
        "recv_rate_mbps": recv_rate_mbps,
        "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S")
    }

# You can add more monitoring functions here, e.g., get_process_list(), get_temperature(), etc.
