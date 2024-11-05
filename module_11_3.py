import inspect


class Cat:
    def __init__(self, name):
        self.name = name

    def mr(self):
        print('Мр-р-р-р')


def introspection_info(obj):
    ans = {}
    ans['type'] = type(obj)
    attr_and_meth = dir(obj)
    attr = []
    meth = []
    for el in attr_and_meth:
        if not callable(getattr(obj, el)):
            attr.append(el)
        else:
            meth.append(el)
    ans['attributes'] = attr
    ans['methods'] = meth
    module = inspect.getmodule(obj)
    if module:
        ans['module'] = module.__name__
    else:
        ans['module'] = None

    if isinstance(obj, str) or isinstance(obj, list):
        ans['len'] = len(obj)
    elif isinstance(obj, int):
        ans['sum'] = sum(int(el) for el in str(obj))
        ans['bin'] = bin(obj)
    return ans


print(introspection_info(13))
print(introspection_info('Ромашки'))
print(introspection_info([1, None, False, 'qwerty', 54.0]))
print(introspection_info(1.1))
cat = Cat('Башмак')
print(introspection_info(Cat))
