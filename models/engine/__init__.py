import .file_storage

storage = file_storage.FileStorage()
storage.reload()
file_storage.storage = storage
