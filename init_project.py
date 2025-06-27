import os

# Folders to create
folders = [
    'data',
    'notebooks',
    'src',
    'tests'
]

# Files to create with optional content
files = {
    'src/__init__.py': '',
    'requirements.txt': '',
    '.gitignore': '*.pyc\n__pycache__/\nvenv/\n.env\n',
    'README.md': '# Claims Litigation Prediction Project\n\nThis project uses AI/ML to predict litigation risk early in workers compensation claims.'
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for filepath, content in files.items():
    with open(filepath, 'w') as f:
        f.write(content)

print("✅ Project structure initialized.")
