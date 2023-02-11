#!/usr/bin/python3
"""create FileStorage instances as part of initialization"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
