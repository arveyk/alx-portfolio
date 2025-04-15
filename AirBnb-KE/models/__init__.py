#!/usr/bin/python3


#from models.engine.file_storage import FileStorage
import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()
storage.reload()
