import time

def timer_decorator(func):
    def wrapper(*args,**kwargs):
        init=time.time()
        results=func(*args,**kwargs)
        fin=time.time()
        exec_time=fin-init
        print(f"Execution time: {exec_time:.2f} seconds")  # Print the execution time
        return results  # Return the result of the original function
    return wrapper
    
@timer_decorator
def factorial(valor):
    resultado=1
    while valor >=1:
        resultado=valor*resultado
        valor=valor-1
    print(resultado)
valor=int(input("Introduzca el valor deseado: "))
factorial(valor)

