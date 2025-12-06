class user_currency():
    def __init__(self, id, user_id, currency_id):
        self.__id = id
        self.__user_id = user_id
        self.__currency_id = currency_id

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        if isinstance(value, str) and len(value) > 1:
            self.__user_id = value
        else:
            raise TypeError("ID должно быть строкой длиной минимум 2 символа")

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
    def currency_id(self):
        return self.__currency_id

    @currency_id.setter
    def currency_id(self, value):
        if isinstance(value, list) and len(value) > 0:
            self.__currency_id = value
        else:
            raise TypeError("ID должно быть строкой длиной минимум 2 символа")

