import os

# Path to the virtual environment's Python executable
venv_python = os.path.abspath("venv/Scripts/python.exe")

# Path to the main script file
main_script = os.path.abspath("main.py")

# Activate the virtual environment
activate_script = os.path.abspath("venv/Scripts/activate")
os.system(f"call {activate_script}")

# Run the main script using the virtual environment's Python executable
os.system(f"{venv_python} {main_script}")
