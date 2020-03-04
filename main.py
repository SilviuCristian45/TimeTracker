import time
from docx import Document

running_state = "true"

#running when the script starts

#running while the script is opened
while True:
    running_state = input("Type false in order to close the program ...")
    #running when the script is closed
    if running_state == "false":
        break

print("-------------   CLOSE PROGRAM   ---------------")