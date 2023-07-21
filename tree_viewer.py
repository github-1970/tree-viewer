import os
import argparse

def display_tree(directory_path, indent=''):
    if not os.path.isdir(directory_path):
        print('This path is not a directory!')
        return

    files = os.listdir(directory_path)
    files.sort()

    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):
            print(indent + '- ' + file)
        elif os.path.isdir(file_path):
            print(indent + '|- ' + file)
            display_tree(file_path, indent + '|  ')

def main():
    parser = argparse.ArgumentParser(description="Display the directory tree.")
    parser.add_argument("directory", help="Path to the target directory")
    args = parser.parse_args()

    target_directory = args.directory
    display_tree(target_directory)

if __name__ == "__main__":
    main()
