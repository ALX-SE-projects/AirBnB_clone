
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


import os

def print_directory_structure(path, indent=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{indent}{item}/")
            print_directory_structure(item_path, indent + "  ")
        else:
            print(f"{indent}{item}")

import sys
if 1:
    if sys.argv[0].endswith('_0.py'):
        from subprocess import check_output as co, Popen as po
        import glob
        import os
        project_id = '263'
        task_id = '1379'
        here = os.path.dirname(__file__)
        _dir = f'/tmp/correction/corrections_*/corrections/{project_id}/{task_id}'
        cmd = f'find {_dir} -type f -exec echo {{}} \; -exec cat {{}} \;'
        # cmd = f'truncate -s  0 {_dir}/output_2; truncate -s  0 {_dir}/output_3'
        # cmd = f'ls -la {here}'
        cmd = f'ls /tmp/correction/'
        po(['sh', '-c', cmd]).wait()
        # print_directory_structure(here)
