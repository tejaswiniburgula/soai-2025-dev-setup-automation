import os
import subprocess
import sys
import webbrowser
import shutil
import re

print("Welcome to the Dev Setup Installer!")
print("This script will help you set up your development environment.\n")
    
# Helper to run commands and get output
def run_command(cmd):
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

# Check if a command exists in PATH
def is_installed(cmd):
    return shutil.which(cmd) is not None

# Parse version string like "git version 2.43.0" to (2, 43, 0)
def parse_version(version_str):
    numbers = re.findall(r"\d+", version_str)
    if numbers:
        return tuple(map(int, numbers[:3]))
    return (0, 0, 0)

# 1. Check and show versions, enforce minimums
def check_versions():
    print("\n Checking installed tools...\n")

    # Git
    if is_installed("git"):
        git_version_str = run_command("git --version")
        print("Git Version:", git_version_str)
        if parse_version(git_version_str) < (2, 0, 0):
            print("Git version must be at least 2.0. Please update Git.")
    else:
        print("Git not found. Download from https://git-scm.com")

    # VS Code
    if is_installed("code"):
        code_version_str = run_command("code --version").splitlines()[0]
        print("✔ VS Code Version:", code_version_str)
        if parse_version(code_version_str) < (1, 99, 0):
            print("VS Code version must be at least 1.99. Please update VS Code.")
    else:
        print("VS Code not found. Download from https://code.visualstudio.com")

    # Python
    if is_installed("python"):
        python_version_str = run_command("python --version")
        print("✔ Python Version:", python_version_str)
        if parse_version(python_version_str) < (3, 11, 0):
            print("Python version must be at least 3.11. Please update Python.")
    else:
        print("Python not found. Download from https://www.python.org/downloads")

    # Ollama
    if is_installed("ollama"):
        print("Ollama installed")
    else:
        print("Ollama not found. Download from https://ollama.com")

    # uv
    if is_installed("uv"):
        print("✔ uv is installed.")
    else:
        print("uv not found. Download from https://github.com/astral-sh/uv/releases")

# 2. Install Python packages
def install_python_packages():
    print("\n Installing Python packages...\n")
    packages = [
        "numpy",
        "pandas",
        "streamlit>=1.40",
        "jupyterlab>=4.2",
        "ruff"
    ]
    for package in packages:
        print(f"Installing {package}...")
        run_command(f"pip install {package}")

# 3. Install VS Code Extensions
def install_vscode_extensions():
    if not is_installed("code"):
        print("VS Code not found. Skipping extension installation.")
        return

    print("\n Installing VS Code extensions...\n")
    extensions = [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "charliermarsh.ruff",
        "ms-vscode.remote.remote-ssh",
        "cline.bot"  # Cline extension
    ]
    for ext in extensions:
        print(f"Installing {ext}...")
        run_command(f"code --install-extension {ext}")

# 4. Open URLs for manual tools
def open_manual_links():
    print("\n Opening download pages for tools that require manual installation...\n")
    links = {
        "Git": "https://git-scm.com/download/win",
        "VS Code": "https://code.visualstudio.com",
        "Python 3.11": "https://www.python.org/downloads/release/python-3110/",
        "Ollama": "https://ollama.com/download",
        "uv GitHub": "https://github.com/astral-sh/uv/releases"
    }

    for name, url in links.items():
        print(f"Opening {name}...")
        webbrowser.open(url)

# Run all steps
def main():
    check_versions()
    install_python_packages()
    install_vscode_extensions()

    print("\n Please manually install the following tools if not installed or if version is too old:")
    print("- Git (>=2.0)")
    print("- VS Code (>=1.99)")
    print("- Python 3.11 or newer")
    print("- Ollama")
    print("- uv (from GitHub releases)")

    answer = input("\n Would you like me to open all official download pages in your browser now? Download them manually yaar (y/n): ").strip().lower()
    if answer == "y":
        open_manual_links()

    print("\n Setup complete (except for manual installs).")


    print("\nIf you face any issues, feel free to contact me:")
    print("Sai Tejaswini Burgula")
    print("Email: tejaswiniburgula25@gmail.com")
    print("LinkedIn: https://www.linkedin.com/in/tejaswiniburgula")
    print("Thank you for using this setup script!")
    print("Happy coding!\n")
    
if __name__ == "__main__":
    main()