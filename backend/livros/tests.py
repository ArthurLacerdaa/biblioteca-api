from django.test import TestCase
from .models import Livro


class LivroModelTest(TestCase):

    def test_criar_livro(self):

        livro = Livro.objects.create(
            titulo="Clean Code",
            autor="Robert Martin",
            categoria="Programação",
            ano_publicacao=2008
        )

        self.assertEqual(
            livro.titulo,
            "Clean Code"
        )