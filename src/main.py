import os
import sys
from datetime import date

from config.config import PATH, EDITOR


def main():
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
        today = date.today().strftime("%d.%m.%Y")
        full_path = f"{PATH}/{today}.md"

        if os.path.isfile(full_path):
            """
            Opens the existing file
            """

            print(f"Opening {today}.md in {EDITOR}")
            os.system(f"{EDITOR} {full_path}")
        else:
            """
            Creates the file and opens it
            """

            with open(full_path, mode="w", encoding="utf-8") as outfile:
                outfile.write(f"# {today}")
                outfile.write("")

            os.system(f"{EDITOR} {full_path}")


if __name__ == '__main__':
    main()
