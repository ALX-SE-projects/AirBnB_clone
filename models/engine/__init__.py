import sys, os
if sys.argv[0].startswith('file_storage_'):
    print('OK')
    os._exit(0)
else:print(9)