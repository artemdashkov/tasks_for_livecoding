
class ContextManager:

    def __init__(self, name):
        print(f"start __init__ method")
        self.name = name

    def __enter__(self):
        print(f"Start __enter__ method")

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Start __exit__ method")



with ContextManager("Ivan") as manager:
    print("Работа внутри контекста")