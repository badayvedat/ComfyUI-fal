import os
import sys
import subprocess

try:
    import fal
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "fal"])
    import fal

script_path = "custom_nodes/ComfyUI-fal-connector/start_server.py"

os.execv(sys.executable, [sys.executable, script_path])
