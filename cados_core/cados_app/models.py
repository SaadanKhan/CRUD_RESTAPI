from django.db import models

class Comapny(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

class Advocate(models.Model): 
    company = models.ForeignKey(Comapny, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username
