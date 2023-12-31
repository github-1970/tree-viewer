import os
import argparse
import zipfile
import tempfile
import shutil
import rarfile


def display_tree(directory_path, indent=""):
    if os.path.isdir(directory_path):
        files = os.listdir(directory_path)
        files.sort()

        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                print(indent + "- " + file)
            elif os.path.isdir(file_path):
                print(indent + "|- " + file)
                display_tree(file_path, indent + "|  ")
    elif zipfile.is_zipfile(directory_path):
        zip_viewer(directory_path)
    elif rarfile.is_rarfile(directory_path):
        rar_viewer(directory_path)
    else:
        print("Error: The provided path is not a valid directory or zip file or rar file.")
        

def zip_viewer(directory_path):
    with zipfile.ZipFile(directory_path, "r") as zip_file:
        temp_dir = tempfile.mkdtemp()
        try:
            zip_file.extractall(temp_dir)
            first_dir = os.listdir(temp_dir)[0]
            display_tree(os.path.join(temp_dir, first_dir))
        finally:
            shutil.rmtree(temp_dir)


def rar_viewer(directory_path):
    with rarfile.RarFile(directory_path, "r") as rar_file:
        temp_dir = tempfile.mkdtemp()
        try:
            rar_file.extractall(temp_dir)
            first_dir = os.listdir(temp_dir)[0]
            display_tree(os.path.join(temp_dir, first_dir))
        finally:
            shutil.rmtree(temp_dir)


def main():
    parser = argparse.ArgumentParser(description="Display the directory tree.")
    parser.add_argument("path", help="Path to the target directory or zip file or rar file")
    args = parser.parse_args()

    target_path = args.path
    display_tree(target_path)


if __name__ == "__main__":
    main()
