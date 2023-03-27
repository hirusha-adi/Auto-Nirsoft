import os
import glob

# Exclude these
EXCLUDE_FILES = ['toPy.py', 'tool.py', 'makeExe']

py_files = glob.glob('*.py')

for py_file in py_files:
    # exclude
    if os.path.basename(py_file) in EXCLUDE_FILES:
        continue
    
    # import and run
    module = __import__(f"{os.path.splitext(py_file)[0].replace('/', '.')}")
    if hasattr(module, 'write'):
        print("saved")
        module.write()
        