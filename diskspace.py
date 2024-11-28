#!/usr/bin/env python3
# Student ID: ajpatel44

import shutil

def check_disk_space(path="/"):
    # Get disk space details
    total, used, free = shutil.disk_usage(path)

    # Convert bytes to human-readable format
    def convert_to_gb(size_in_bytes):
        return size_in_bytes / (1024 ** 3)

    print(f"Disk Space on {path}:")
    print(f"Total: {convert_to_gb(total):.2f} GB")
    print(f"Used: {convert_to_gb(used):.2f} GB")
    print(f"Free: {convert_to_gb(free):.2f} GB")

