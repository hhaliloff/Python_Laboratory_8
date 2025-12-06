from http.server import HTTPServer, BaseHTTPRequestHandler
from models import user, user_currency, app, author, currency
from utils.currencies_api import get_currencies
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from urllib.parse import urlparse, parse_qs
from static.currency_id import get_ids

actual_author = author("Чингиз Халилов", "P3122")
actual_app = app("StuxNet", "0.1(alpha)", actual_author)
ids = get_ids()
currencies = get_currencies(ids)
user1 = user_currency("504634", "Chingiz", ["USD", "EUR"])
user2 = user_currency("505301", "Ivan", ["JPY", "CNY"])
user3 = user_currency("504695", "Milana", ["GBP", "AUD"])
users = [user1, user2, user3]
subs = []

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/action":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = parse_qs(body)

            button = data.get("subscription", [""])[0]
            subs.append(button)
            print("Пользователь нажал кнопку:", button)
            print(subs)
            self.send_response(302)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Location", "/currencies")
            self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query_params = parse_qs(parsed.query)

        if path == "/":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            result = env.get_template("index.html").render(myapp=actual_app.name,
                      author_name = actual_author.name,
                      group = actual_author.group,
                                     version = actual_app.version, subs = subs, currency = currencies
                                     )
            self.wfile.write(bytes(result, "utf-8"))

        if path == "/currencies":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            result = env.get_template("currencies.html").render(ids=ids, currency=currencies, subs=subs)
            self.wfile.write(bytes(result, "utf-8"))


        if path == "/author":
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            result = env.get_template("author.html").render(author = actual_author.name, group = actual_author.group)
            self.wfile.write(bytes(result, "utf-8"))


        if path == "/user" and "id" in query_params:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            if query_params["id"][0] == "0":
                result = env.get_template("users.html").render(user1 = user1.user_id, user2 = user2.user_id, user3 = user3.user_id)
            users_id = [i.id for i in users]
            if ''.join(query_params["id"]) in users_id:
                user_in = users_id.index(''.join(query_params["id"]))
                result = env.get_template("one_user.html").render(name=users[user_in].user_id, user_cur = users[user_in].currency_id, currencies = currencies)
            self.wfile.write(bytes(result, "utf-8"))




env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", 8000), MyHandler)
    print("Server is running on http://localhost:8000")
    httpd.serve_forever()
