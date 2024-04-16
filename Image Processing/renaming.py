# Replacing dash to underscore (Usually for bulk image import)

import os

# TODO: Change the directory
directory_path = r'C:\Users\Krischelle Cadao\Downloads\drive-download-20240401T191427Z-001\bulk1'

for root, _, filenames in os.walk(directory_path):
    for filename in filenames:
        old_path = os.path.join(root, filename)
        new_filename = filename.replace('-', '_')
        new_path = os.path.join(root, new_filename)
        os.rename(old_path, new_path)
