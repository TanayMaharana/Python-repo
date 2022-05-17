#!/usr/bin/env python3
import psutil
import shutil
import os
import sys

def check_reboot():
  return os.path.exists("/run/reboot-required")

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free/du.total*100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return usage < 75

def main():
  if not check_disk_usage("/") and check_cpu_usage():
    print("ERROR in the system!")
    sys.exit(2)
  if check_reboot():
    print("Reboot Required.")
    sys.exit(1)
  else:
    print("Everything is working fine.")

main()
