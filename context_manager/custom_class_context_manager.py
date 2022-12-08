class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, *args, **kwargs):
        self.file.close()


with OpenFile("files/custom_context_manager", "w") as f:
    f.write("Good realize with custom context manager")

print(f.closed)