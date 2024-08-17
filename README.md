# File sorter
To sort images and videos into folders by year and month

# Installation
Install python globally if not already installed.

Download and unzip from github to a desired location or clone read only from github.

Open the installation location in command terminal and run:
```python -m venv .venv```

After creating venv install the requirements with
```.venv\Sripts\activate && pip install -r requirements.txt```

# Usage

run with this:

```.venv\Sripts\python.exe <source_path> <destination_path> <file_type> <mode>```

Use absolute paths.
supported file type options: image, video
supported mode options: month_sort
