from django.db import models

class User(models.Model): 

    user = models.CharField(max_length = 100, unique = True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.user