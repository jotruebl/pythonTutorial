# def decorator_function(original_function):
#     def wrapper(*args, **kwargs):
#         print('wrapper executed before '+ f'{original_function.__name__}')
#         return original_function(*args, **kwargs)
#     return wrapper

# @decorator_function
# def display(age1, age2):
#     x=age1 + age2
#     return(x)

# # this will return the result wrapper function, which we then
# # execute using the () 
# #display = decorator_function(display) # shorthand can be the @
# hey=display(5, 10)
# print(hey)
# # so now hey is the result of running display wrapped in the wrapper.


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args {args} and {kwargs}'
        )
        return orig_func(*args, **kwargs)
    return wrapper

@my_logger
def simple(*args,**kwargs):
    z = args[0]+args[1]
    return(z)


result=simple(5,3,6,2,1, jon='cool')
print(result)
