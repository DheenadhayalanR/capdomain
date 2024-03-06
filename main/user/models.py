from django.db import models


class UserLogin(models.Model):
      
      user_name=models.CharField(max_length=20)
      email_address=models.EmailField()
      password=models.CharField(max_length=20)
