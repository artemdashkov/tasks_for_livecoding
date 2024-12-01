from datetime import  datetime

def decorator_func(func):
    print("Старт декоратора")
    def new_func():
        print("Старт программы")
        func()
        print("Концовка программы")
    return new_func

@decorator_func
def prosto_programm():
    print("Этот принт из 'prosto_programm()' func")

prosto_programm()

def decorator_time(func):
    def wrapper():
        start_time = datetime.now()
        print(f"start_time: \t{start_time}")
        func()
        end_time = datetime.now()
        print(f"start_time: \t{end_time}")
        total_time = end_time - start_time
        print(f"total_time: \t{total_time}")
    return wrapper

@decorator_time
def prosto_programm_2():
    print("Этот принт из 'prosto_programm()' func")

prosto_programm_2()