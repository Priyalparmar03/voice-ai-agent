def validate(tasks):
    for t in tasks:
        if "filename" in t and ".." in t["filename"]:
            return False, "Unsafe path"
    return True, "Safe"