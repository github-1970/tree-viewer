import os
import argparse
import zipfile
import tempfile
import shutil

def display_tree(directory_path, indent=''):
    if os.path.isdir(directory_path):
        files = os.listdir(directory_path)
        files.sort()

        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                print(indent + '- ' + file)
            elif os.path.isdir(file_path):
                print(indent + '|- ' + file)
                display_tree(file_path, indent + '|  ')
    elif zipfile.is_zipfile(directory_path):
        with zipfile.ZipFile(directory_path, 'r') as zip_file:
            temp_dir = tempfile.mkdtemp()
            try:
                zip_file.extractall(temp_dir)
                first_dir = os.listdir(temp_dir)[0]
                display_tree(os.path.join(temp_dir, first_dir))
            finally:
                shutil.rmtree(temp_dir)

def main():
    parser = argparse.ArgumentParser(description="Display the directory tree.")
    parser.add_argument("path", help="Path to the target directory or zip file")
    args = parser.parse_args()

    target_path = args.path
    display_tree(target_path)

if __name__ == "__main__":
    main()
