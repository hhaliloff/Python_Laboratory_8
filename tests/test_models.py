import os
import sys
import unittest

# Добавляем корень проекта в sys.path
CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from models.user import user   # твой класс user из models/user.py


class TestUserModel(unittest.TestCase):

    def test_getters(self):
        """
        Проверка геттеров: корректные значения после создания объекта.
        """
        u = user("123456", "Иван")

        self.assertEqual(u.id, "123456")
        self.assertEqual(u.name, "Иван")

    def test_invalid_id_setter(self):
        """
        Проверка выброса исключений при некорректном ID.
        ID должен быть строкой длиной минимум 6 символов.
        """
        u = user("123456", "Иван")

        # Слишком короткий ID
        with self.assertRaises(TypeError):
            u.id = "123"

        # Не строка
        with self.assertRaises(TypeError):
            u.id = 123456

    def test_invalid_name_setter(self):
        """
        Проверка выброса исключений при некорректном имени.
        Имя должно быть строкой длиной минимум 2 символа.
        """
        u = user("123456", "Иван")

        # Слишком короткое имя
        with self.assertRaises(TypeError):
            u.name = ""

        # Не строка
        with self.assertRaises(TypeError):
            u.name = 123


if __name__ == "__main__":
    unittest.main()
