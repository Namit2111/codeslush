import subprocess
import os

def get_python_code_from_repo(repo_url, clone_path):
    # Clone the repository
    try:
        subprocess.run(["git", "clone", repo_url, clone_path], check=True)
        print(f"Repository cloned to {clone_path}")
    except subprocess.CalledProcessError as e:
        return f"Error cloning repository: {e}"

    # Read all .py files from the repository
    code = ""
    for root, dirs, files in os.walk(clone_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code += f.read() + "\n"  # Add newline to separate file contents
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    # Optionally, clean up by removing the cloned repository
    # import shutil
    # shutil.rmtree(clone_path)

    return code
