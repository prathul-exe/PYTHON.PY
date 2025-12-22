#📂File Sorter
"""
This is a file sorter that sorts different file types into folders.A .bat file can be included for this to be
directly executed via cmd without using a code editor.This minimises the effort if sorting files manually.This helps in keeping the computer
organized and clean.
---22-12-2025
"""

from pathlib import Path
import os
import shutil
spot=input("Enter Spot to be sorted(Downloads,Desktop,Pictures,Music,Videos):")
# 📦 Global Path
path = Path.home() / spot

# 🔎 Sorting Rules
CATEGORIES = {
    "_Images": ['.jpg', '.jpeg', '.png'],
    "_GIF": ['.gif'],
    "_Videos": ['.mp4', '.mkv', '.avi', '.mov'],
    "_Docs": ['.pdf', '.docx', '.txt'],
    "_ZIPs": ['.zip', '.rar', '.7z'],
    "_Installers": ['.exe', '.msi'],
    "_Code": ['.py', '.js', '.html', '.css', '.md', '.keras'],
    "_Data": ['.csv', '.xlsx']
}

def get_file_cat(file):
    # Ignore already sorted folders
    if file.startswith('_'):
        return None

    filepath = path / file

    # If it's a folder
    if filepath.is_dir():
        return "_Folders"

    # If it's a file
    file_extension = filepath.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if file_extension in extensions:
            return category

    print(f"❓ Unsupported file type: {file}")
    return "_Others"


# 📚 Read & Sort Files
for file in os.listdir(path):
    dir_name = get_file_cat(file)

    if dir_name:
        dir_path = path / dir_name
        dir_path.mkdir(exist_ok=True)

        old_path = path / file
        new_path = dir_path / file

        try:
            shutil.move(str(old_path), str(new_path))
            print(f"➡️ {dir_name}/{file}")
        except Exception as e:
            print(f"❌ {file} - {e}")
