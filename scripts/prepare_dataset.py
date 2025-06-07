from pathlib import Path
from PIL import Image
import re

input_dir = Path("/work3/s234843/02466-Project/dataset/fluorescent/without_masks")
output_dir = Path("/work3/s234843/02466-Project/dataset/fluorescent/without_masks_224")
output_dir.mkdir(parents=True, exist_ok=True)

count = 0  # Add before the loop

for tif_path in input_dir.glob("*.tif"):
    # Extract the time component from filename using regex
    match = re.search(r"_(\d{2})h(\d{2})m(\d{2})s_", tif_path.name)
    if not match:
        continue  # Skip files without a valid time format

    hours = int(match.group(1))
    
    if hours >= 29:
        img = Image.open(tif_path)
        img = img.resize((224, 224), Image.BICUBIC)
        out_path = output_dir / tif_path.with_suffix(".png").name
        img.save(out_path)
        count += 1
        if count >= 3000:
            break

print(f"Resized images saved to: {output_dir}")
