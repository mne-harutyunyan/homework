import time
def memoize(func):
  cache = {}
  def wrapper(n):
    if not n in cache:
      result = func(n)
      cache[n] = result
    return cache[n]
  return wrapper

@memoize
def factorial(n):
  return 1 if n <= 1 else n * factorial(n - 1)

start1 = time.time()
a = factorial(10)
end1 = time.time() - start1

start2 = time.time()
b = factorial(6)
end2 = time.time() - start2
print(end1>end2)






