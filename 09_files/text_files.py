# In JS (Node): fs.writeFileSync() / fs.readFileSync()
# In Python: 'with open()' automatically closes the file when done!
from pathlib import Path

file_path = Path("sample.txt")

# Write to file
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello from Python\nLine 2: File handling is easy\n")

# Read file
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        print("Read line:", line.strip())

# Clean up
if file_path.exists():
    file_path.unlink()
