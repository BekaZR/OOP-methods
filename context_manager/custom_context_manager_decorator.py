from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with open_file("files/custom_context_manager_decorator", "w") as f:
    f.write("Good realize with custom context manager decorator")


print(f.closed)