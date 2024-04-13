import urllib.request
import os
from pathlib import Path
import shutil


class Files:
    src_base_path: str
    dest_base_path: str

    def __init__(self, src_base_path: str, dest_base_path: str):
        self.src_base_path = src_base_path
        self.dest_base_path = dest_base_path

    def clean(self):
        shutil.rmtree(self.dest_base_path)

    def copy_url(self, path: str):
        dest = Path(self.dest_base_path + path)
        os.makedirs(dest.parent)
        urllib.request.urlretrieve(
            self.src_base_path + path,
            dest
        )

