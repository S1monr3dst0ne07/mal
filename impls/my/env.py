


class Env:
    def __init__(self, outer, binds=[], exprs=[]):
        self.outer = outer
        self.data  = {}

        for (key, obj) in zip(binds, exprs):
            self.set(key.content, obj)


    def set(self, key, obj):
        self.data[key] = obj

    def get(self, key):
        if key in self.data:
            return self.data[key]

        elif self.outer:
            return self.outer.get(key)

        else:
            raise Exception(f"'{key}' not found")



