class author():
    def __init__(self, name, group):
        self.__name = name
        self.__group = group

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
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        if isinstance(value, str) and len(value) > 4:
            self.__group = value
        else:
            raise TypeError("Группа должна быть строкой длиной минимум 5 символов")