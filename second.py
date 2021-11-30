def my_func(*args,**kwargs):
    print(args)
    print("Welcome to the world of git repositories")

def outer(fn):
    def inner(*args,**kwargs):
        print("Within inner")
        return fn(*args,**kwargs)
    return inner
my_func=outer(my_func)


my_func('GIT','Version','Controller')