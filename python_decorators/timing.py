import functools, time

def timer(func):
    '''Print the runtime of the decorated function'''
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} seconds.')
        #print(value)
        return value
    return wrapper_timer

@timer
def waste_time(num_times):
    variable = 5+10
    return variable
    
#a=waste_time(5)

def debug(func)
    @functools.wraps(fun)
    def wrapper_debug(*args, **kwargs):
        args_repr [ repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k,v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    else:
        return f'Whoa {name}! {age} already?'

