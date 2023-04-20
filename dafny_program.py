class Type:
    def isPrintable(self):
        pass


class BaseType(Type):
    def __init__(self):
        self.name = None

    def set_name(self, name: str):
        self.name = name

    def isPrintable(self):
        return self.name != "real"


class CollectionType(Type):
    def __init__(self):
        self.name = None
        self.inner_types = []

    def set_name(self, name: str):
        self.name = name

    def get_inner_type(self):
        return self.inner_types[0]

    def add_inner_type(self, type: Type):
        self.inner_types.append(type)

    def isPrintable(self):
        if self.name == "set" or self.name == "multiset" or self.name == "array" or self.name == "map":
            return False
        if len(self.inner_types) == 0:
            return False

        for t in self.inner_types:
            if not t.isPrintable():
                return False
        return True
