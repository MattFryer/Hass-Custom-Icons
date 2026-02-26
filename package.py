import gzip
import os
import shutil

source_file = "Hass-Custom-Icons.js"
output_file = "Hass-Custom-Icons.js.gz"

if os.path.exists(output_file):
    os.remove(output_file)
    print(f"Deleted existing {output_file}")

with open(source_file, "rb") as f_in:
    with gzip.open(output_file, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

print(f"Created {output_file}")
