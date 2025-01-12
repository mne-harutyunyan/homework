# Իրականացնել դեկորատոր @measure_time, որը կչափի ֆունկցիայի կատարման և տպագրման ժամանակը: 
# Դեկորատորը պետք է կիրառելի լինի ցանկացած ֆունկցիայի համար։
import time
def measure_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(6)
        result = function(*args, **kwargs)
        end = time.time() - start
        print(end)
        return result
    return wrapper

@measure_time
def foo():
    print("Hello user jan")

foo()
