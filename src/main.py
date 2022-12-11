import os
import sys
from datetime import date

from config.config import PATH, EDITOR

if PATH is None and EDITOR is None:
    print("First time using?")
    print("Please set your PATH to where to output diary files and your main editor via App/src/config.py")
    sys.exit()

elif PATH is None:
    print("Please set your PATH to where to output diary files via App/src/config.py")
    sys.exit()

elif EDITOR is None:
    print("Please set your main text editor for how to open your diary files via App/src/config.py")
    sys.exit()

else: 
    # day.month.year format
    today = date.today().strftime("%d.%m.%Y")

    full_path = f"{PATH}/{today}.md"
    if os.path.isfile(full_path):
        print(f"Opening {today}.md in {EDITOR}")
        os.system(f"{EDITOR} {full_path}")
    else:    
        with open(full_path, mode="w", encoding="utf-8") as outfile:
            outfile.write(f"# {today}")
            outfile.write("")

        os.system(f"{EDITOR} {full_path}")