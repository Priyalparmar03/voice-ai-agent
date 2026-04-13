import os

os.makedirs("output", exist_ok=True)

def create_file(name):
    if ".." in name:
        return "Unsafe filename"

    path = os.path.join("output", name)

    if os.path.exists(path):
        return "File already exists"

    with open(path, "w") as f:
        f.write("")

    return f"Created {path}"

def write_file(name, content):
    path = os.path.join("output", name)

    with open(path, "w") as f:
        f.write(content)

    return f"Written {path}"