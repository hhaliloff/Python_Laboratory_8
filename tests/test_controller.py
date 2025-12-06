import os
import sys
import unittest
from io import BytesIO

CURRENT_DIR = os.path.dirname(__file__)
ROOT = os.path.dirname(CURRENT_DIR)
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from myapp import MyHandler, user1, users


class FakeSocket:
    def makefile(self, *args, **kwargs):
        return BytesIO()


class TestController(unittest.TestCase):

    def make_handler(self, path: str) -> MyHandler:
        """
        Создаём экземпляр MyHandler так, как будто к нему пришёл HTTP-запрос.
        """
        request_text = f"GET {path} HTTP/1.1\r\nHost: localhost\r\n\r\n".encode("utf-8")
        fake_rfile = BytesIO(request_text)
        fake_wfile = BytesIO()

        handler = MyHandler(
            request=FakeSocket(),
            client_address=("127.0.0.1", 8000),
            server=None,
        )

        handler.rfile = fake_rfile
        handler.wfile = fake_wfile
        handler.raw_requestline = handler.rfile.readline()
        handler.parse_request()
        return handler

    def get_body(self, handler: MyHandler) -> str:
        """
        Достаём только тело ответа (без статусной строки и заголовков).
        """
        raw = handler.wfile.getvalue().decode("utf-8")
        # отделяем заголовки от тела
        if "\r\n\r\n" in raw:
            _, body = raw.split("\r\n\r\n", 1)
        else:
            body = raw
        return body

    def test_index_route(self):
        """Проверка маршрута '/' — главная страница отдается без ошибок."""
        handler = self.make_handler("/")
        handler.do_GET()

        body = self.get_body(handler).lower()
        # Проверяем, что это HTML-страница и там есть что-то про приложение/автора
        self.assertIn("<html", body)
        self.assertIn("</html>", body)

    def test_currencies_route(self):
        """Проверка маршрута '/currencies'."""
        handler = self.make_handler("/currencies")
        handler.do_GET()

        body = self.get_body(handler).lower()
        # В твоём шаблоне есть заголовок "списки валют:"
        self.assertIn("списки валют", body)
        # и хотя бы один код валюты, например usd/eur
        self.assertTrue("usd" in body or "eur" in body)

    def test_author_route(self):
        """Проверка маршрута '/author'."""
        handler = self.make_handler("/author")
        handler.do_GET()

        body = self.get_body(handler).lower()
        # В шаблоне явный заголовок "автор сие чудесного приложения"
        self.assertIn("автор", body)
        self.assertIn("группа", body)

    def test_user_route_valid(self):
        """
        Проверка маршрута '/user' с корректным id пользователя.
        В myapp.py поиск идёт по полю i.id, а в шаблон передаётся user_id.
        """
        # Берём существующий id из списка users
        existing_id = users[0].id   # строка типа "504634"
        expected_name = users[0].user_id  # например "Chingiz"

        handler = self.make_handler(f"/user?id={existing_id}")
        handler.do_GET()

        body = self.get_body(handler)
        # Ожидаем, что в ответе есть имя пользователя
        self.assertIn(expected_name, body)

    def test_user_route_invalid(self):
        """
        Проверка обработки некорректного id.
        Текущая реализация myapp.py выбрасывает UnboundLocalError
        при id, которого нет в users_id — тест фиксирует это поведение.
        """
        handler = self.make_handler("/user?id=999999")
        with self.assertRaises(UnboundLocalError):
            handler.do_GET()


if __name__ == "__main__":
    unittest.main()
