from django.db import models


class Snippet(models.Model):
    language = models.CharField(max_length=20, default='')
    code = models.TextField(default='')

    def is_cpp(self):
        return self.language == 'cpp'


# python manage.py makemigrations snippets
# python manage.py migrate