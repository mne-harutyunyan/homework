# Develop a generator function custom_zip(*iterables) that mimics the behavior of the built-in zip() function.
#  It should yield tuples containing items from each iterable passed as arguments, stopping when
#  the shortest iterable is exhausted. Test your generator with two or more lists of different lengths.


def custom_zip(*iterables):
    min_lenght = len(iterables[0])
    for item in range(len(iterables)):
        if min_lenght > len(iterables[item]):
            min_lenght = len(iterables[item])
    for i in range(min_lenght):
        result=tuple([iterable[i] for iterable in iterables])
        yield result

ls1=[1,2,3,4]
ls2=[5,3,4,5,6,7]
ls3=['hello','bye',"Bob","world"]

generator = custom_zip(ls1,ls2,ls3)
for i in generator:
    print(i)