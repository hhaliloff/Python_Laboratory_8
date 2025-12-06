class currency():
    def __init__(self, id, num_code, char_code, name, value, nominal):
        self.__name = name
        self.__id = id
        self.__num_code = num_code
        self.__char_code = char_code
        self.__value = value
        self.__nominal = nominal

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
            self.__id = value
        else:
            raise TypeError("ID должен быть строкой длиной минимум 6 символов")

    @property
    def num_code(self):
        return self.__num_code

    @num_code.setter
    def num_code(self, value):
        if isinstance(value, str) and len(value) > 2:
            self.__num_code = value
        else:
            raise TypeError("Num_code должен быть строкой длиной минимум 3 символа")

    @property
    def char_code(self):
        return self.__char_code

    @char_code.setter
    def char_code(self, value):
        if isinstance(value, str) and len(value) > 2:
            self.__char_code = value
        else:
            raise TypeError("Char_code должен быть строкой длиной минимум 3 символов")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str) and len(value) > 3:
            self.__value = value
        else:
            raise TypeError("Value должен быть строкой длиной минимум 4 символа")

    @property
    def nominal(self):
        return self.__nominal

    @nominal.setter
    def nominal(self, value):
        if isinstance(value, int) and value > 0:
            self.__nominal = value
        else:
            raise TypeError("Nominal должен быть числом больше 0 ")