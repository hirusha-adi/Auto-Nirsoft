import os
import base64

# Executable Name representing the current executable data
EXE_NAME = """DATA"""

# Base64 encoded raw bytes of the original .exe file 
EXE_DATA = r"""DATA"""

# Dump EXE_DATA to EXE_NAME file
def write(): 
    with open(EXE_NAME, "wb") as file: 
        # Decode the Base64 and write bytes to file
        file.write(base64.b64decode(EXE_DATA))
        
if __name__ == "__main__": 
    write()
