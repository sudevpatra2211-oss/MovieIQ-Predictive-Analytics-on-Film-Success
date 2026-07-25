#!/usr/bin/env python3
"""
Streamlit Cloud Deployment Alias
This file serves as an entry point for cloud deployments.
It imports and runs the main app.py
"""

import subprocess
import sys
import os

# Ensure we're in the right directory
if __name__ == "__main__":
    # Run the main app
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
