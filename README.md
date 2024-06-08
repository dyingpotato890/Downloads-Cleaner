# Downloads Cleaner

Downloads Cleaner is a simple and efficient tool to help you keep your Downloads folder organized by automatically sorting and managing files based on their types.

## Table of Contents

1. [Features](#features)
2. [Folder Structure](#folder-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [License](#license)

## Features

- Automatically moves files to appropriate subfolders (e.g., Documents, Images, Videos)
- Customizable file type categories
- Easy to set up and run

## Folder Structure

```
Downloads/
├── Audios/
│ ├── audio1.pdf
│ ├── audio2.docx
│ └── ...
├── Documents/
│ ├── file1.pdf
│ ├── file2.docx
│ └── ...
├── Images/
│ ├── image1.jpg
│ ├── image2.png
│ └── ...
├── Videos/
│ ├── video1.mp4
│ ├── video2.avi
│ └── ...
├── Executables/
│ ├── package1.exe
│ ├── package2.exe
│ └── ...
├── Compressed Files/
│ ├── archive1.zip
│ ├── archive2.rar
│ └── ...
├── Program Code/
│ ├── code1.py
│ ├── code2.c
│ └── ...
└── Random/
├── file1.exe
├── file2.bin
└── ...
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dyingpotato890/Downloads-Cleaner.git
    cd Downloads-Cleaner
    ```

## Usage

1. Ensure the `downloadsCleaner.py` script is executable:
    ```bash
    chmod +x downloadsCleaner.py
    ```

2. Run the script:
    ```bash
    python downloadsCleaner.py
    ```

## Configuration

You can customize the file type categories by editing the file extension lists in the script. The default configuration includes common file types and their destinations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
