from pathlib import Path

files = Path().glob('*.slides.html')
for file in files:
    with open(file, 'r') as f:
        text = f.read()

    with open(file, 'w') as f:
        f.write(text.replace('<head>', '<head><link rel="stylesheet" href="rise.css">'))
