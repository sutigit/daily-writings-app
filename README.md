# Daily writes

This App generates a new diary page everytime you invoke the app. The blank page is an markdown file with only the current date as the headline. If there already exists a file with the current date, the app will open that file. Otherwise the app will generate a new file with new current date on the next day.

## Python version
Check your python version. This app has been tested on python3 version 3.8^

## Documentation
[Features](https://github.com/sutigit/daily-writings-app/blob/main/features)

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

Run
```
poetry run invoke start
```
