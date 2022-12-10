# App

This App generates a new diary page everytime you invoke the app. The blank page is an markdown file with only the current date as the headline. If there already exists a file with the current date, the app will open that file. Otherwise the app will generate a new file with new current date on the next day.

## Python version
Check your python version. This app has been tested on python3 version 3.8^

## Documentation
[Features](https://github.com/sutigit/daily-writings-app/blob/main/documentation/features.md)

## Running the app
Download the app and extract

Make sure you have poetry installed. 
```
poetry --version
```

Go to App folder
```
cd App
```

Run 
```
poetry install
```

Go to config/config.py and give terminal command to your text editor and outputh path for your diary files.
```
# Choose your main editor to open the diary pages
# example "nano" for nano editor or "code" for vscode
EDITOR = "example"

# Choose your directory to where to create diary templates
PATH = "/home/example/directory"
```


Run
```
poetry run invoke start
```

## Usage
I recommend to have an alias for starting the app. 
Example command: "cd %PATH%/App && poetry run invoke start"

