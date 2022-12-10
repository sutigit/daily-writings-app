
import sys
from datetime import date

from config import PATH, EDITOR

# if PATH is None and EDITOR is None:
#     print("First time using?")
#     print("Please set your PATH to where to output diary files and your main editor via App/src/config.py")
#     sys.exit()

# elif PATH is None:
#     print("Please set your PATH to where to output diary files via App/src/config.py")
#     sys.exit()

# elif EDITOR is None:
#     print("Please set your main text editor for how to open your diary files via App/src/config.py")
#     sys.exit()

# dd/mm/YY
today = date.today().strftime("%d/%m/%Y")
print(PATH, EDITOR)

print("shiiiit")