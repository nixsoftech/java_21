import subprocess
import psutil
import time
import os

# Path to your application
APP_PATH = r"D:\Program Files (x86)\NCCL Ltd\RMSSetup\RMS FE.exe"

# Launch application
proc = subprocess.Popen([APP_PATH])
print(f"App started with PID: {proc.pid}")

# Wait for app to load
time.sleep(5)

# Check if process is running
if psutil.pid_exists(proc.pid):
    print("App is running...")
else:
    print("App failed to start!")

# Monitor (example: run for 10 seconds then close)
time.sleep(10)

# Kill process using psutil
p = psutil.Process(proc.pid)
p.terminate()
p.wait()
print("App closed successfully.")
