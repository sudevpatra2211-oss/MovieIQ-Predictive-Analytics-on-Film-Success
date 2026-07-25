# This file is an alias to app.py for Streamlit Cloud deployment
import subprocess
import sys

subprocess.run([sys.executable, "app.py"])
