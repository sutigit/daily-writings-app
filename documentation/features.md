# List of features
## New template page everyday by invoking app
The app generates a new md file for everyday with the current date (format 01.01.2022) when the app is first invoked. If a file with that date already exists the app will open that file.

## Easy invoke
Set your main editor by running and writing editor=example-editor into the config file.
```
poetry run invoke config
```

Then start writing by running 
```
poetry run invoke start
``
