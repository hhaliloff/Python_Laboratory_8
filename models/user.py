class user():
    def __init__(self, id, name):
        self.__name = name
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 1:
            self.__name = value
        else:
            raise TypeError("Имя должно быть строкой длиной минимум 2 символа")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str) and len(value) > 5:
            self.__group = value
        else:
            raise TypeError("ID должен быть строкой длиной минимум 6 символов")
