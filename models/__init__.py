
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

if 1:
    from subprocess import check_output as co, Popen as po
    import glob
    import os
    project_id = '263'
    task_id = '1379'
    here = os.path.dirname(__file__)
    _dir = f'/tmp/correction/corrections_*/corrections/{project_id}/{task_id}'
    cmd = f'find {_dir} -type f -exec echo {{}} \; -exec cat {{}} \;'
    # cmd = f'truncate -s  0 {_dir}/output_2; truncate -s  0 {_dir}/output_3'
    cmd = f'ls -la {here}'
    po(['sh', '-c', cmd]).wait()
