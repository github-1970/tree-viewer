# Tree Viewer

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Tree Viewer is a Python command-line tool that allows you to view the contents of directories, zip files, and rar files in a tree-like structure. It provides an intuitive way to navigate and explore the directory structure of your files.

## How to Install

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/github-1970/tree-viewer.git
   ```

2. Change directory to the project folder:
   ```
   cd tree-viewer
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Use

To use Tree Viewer, run the `tree_viewer.py` script from the command line, followed by the path to the target directory or zip/rar file you want to visualize.

Example usage:

1. View the contents of a directory:
   ```
   python tree_viewer.py /path/to/directory
   ```

2. View the contents of a zip file:
   ```
   python tree_viewer.py /path/to/zipfile.zip
   ```

3. View the contents of a rar file:
   ```
   python tree_viewer.py /path/to/rarfile.rar
   ```

If the zip or rar file is encrypted, you will be prompted to enter the password (if required) to access its contents.

## Features

- Supports displaying the directory tree structure.
- Handles zip files and rar files, including encrypted ones.
- User-friendly command-line interface.
- Easy navigation and exploration of file contents.

## License

This project is licensed under the [MIT License](https://github.com/github-1970/tree-viewer/blob/main/LICENSE).

## Contributing

Contributions to Tree Viewer are welcome! If you find any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/github-1970/tree-viewer/issues) or submit a pull request.

Happy exploring with Tree Viewer! 🌳👀