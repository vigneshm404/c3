object = {"a":{"b":{"c":"d"}}}
key = 'a/b/c'
def get_value(object,key):
    object1 = object
    key1 = key.split('/')
    for i in key1:
        object1 = object1.get(i)
    return object1
value=get_value(object,key)
print(value)
