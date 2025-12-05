from laba_8.myapp.models.author import author

class app():
    def __init__(self, name, version, author):
        self.__name = name
        self.__version = version

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 1:
            self.__name = value
        else:
            raise TypeError("Имя приложения должно быть строкой длиной минимум 2 символа")

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        if isinstance(value, str) and len(value) > 1:
            self.__version = value
        else:
            raise TypeError("Имя версии должно быть строкой длиной минимум 2 символа")

    @property
    def author(self):
        return self.__author

    @author.setter
    def version(self, value):
        if isinstance(value, author):
            self.__version = value
        else:
            raise TypeError("Имя версии должно быть строкой длиной минимум 2 символа")