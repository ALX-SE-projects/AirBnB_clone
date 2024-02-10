
from .engine.file_storage import FileStorage

storage = FileStorage(file_path="file.json")
storage.reload()