import os, base64


def loadContentToPy(fname: str, fpath_exe: str) -> str:
    
    savename = os.path.join(os.getcwd(),''.join(os.path.split(fpath_exe)[-1].split(".exe")) + ".py")
    
    with open(fpath_exe, "rb") as file:
        content = file.read()
        encoded = base64.b64encode(content)

    with open(savename, 'w+') as temp_file:
        temp_file.write(f'''import os, base64
EXE_NAME = """{fname}"""
EXE_DATA = {encoded}
def write(): 
    with open(EXE_NAME, "wb") as file: file.write(base64.b64decode(EXE_DATA))
if __name__ == "__main__": write()''')

    return savename


path = os.getcwd()
if os.path.exists("tools"):
    path = os.path.join(os.getcwd(), "tools")

for name in os.listdir(path):
    if os.path.isfile(name) and name.lower().endswith(".exe"):
        try:
            current_exe_dir = os.path.join(os.getcwd(), name)
            loadContentToPy(fname=name, fpath_exe=current_exe_dir)
            break
        except Exception as e:
            print(e)
            break
            # continue
