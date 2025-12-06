import unittest
from jinja2 import Environment


env = Environment()


class TestTemplates(unittest.TestCase):

    def test_template_variables(self):
        """Переменные корректно подставляются в шаблон."""
        template = env.from_string("{{ username }}: {{ value }}")
        rendered = template.render(username="user1", value=42)
        self.assertEqual(rendered, "user1: 42")

    def test_template_loop(self):
        """Рендеринг цикла for."""
        template = env.from_string("{% for item in items %}{{ item }} {% endfor %}")
        rendered = template.render(items=[1, 2, 3])
        self.assertEqual(rendered.strip(), "1 2 3")

    def test_template_condition(self):
        """Рендеринг условий if/else."""
        template = env.from_string("{% if is_admin %}admin{% else %}user{% endif %}")

        admin_html = template.render(is_admin=True)
        user_html = template.render(is_admin=False)

        self.assertEqual(admin_html, "admin")
        self.assertEqual(user_html, "user")


if __name__ == "__main__":
    unittest.main()
