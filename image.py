from PIL import Image
import os

input_dir = "./assets"
output_dir = "./compressed"

# Create output folder if it doesn’t exist
os.makedirs(output_dir, exist_ok=True)

extensions = (".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG")

for filename in os.listdir(input_dir):
    if not filename.endswith(extensions):
        continue

    input_path = os.path.join(input_dir, filename)
    root, _ = os.path.splitext(filename)
    output_path = os.path.join(output_dir, f"{root}.jpg")

    try:
        with Image.open(input_path) as img:
            rgb_img = img.convert("RGB")
            rgb_img.save(output_path, "JPEG", quality=75, optimize=True)
            print(f"✅ {filename} → {output_path}")
    except Exception as e:
        print(f"⚠️ Error processing {filename}: {e}")

print("🎉 All images converted and compressed to ./compressed")
