from django.db import models 

from django.contrib.auth.models import User, AbstractUser

# Create your models here.

"""
Class AbstractUser, atributos que podemos heredar:
username
first_name
last_name
email
password
groups
user_permissions
is_staff
is_active
is_superuser
last_login
date_joined
"""

"""Class AbstractBaseUser, atributos que podemos heradar:
id
paswword
last_login
"""

class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


# proximodel Customer exiente funcionalidades del modelo User
class Customer(User):
    
    class Meta:
        proxy = True
        
    def get_products(self):
        return []
    

# Profile extiende atributos de User mediante relacion 1-1
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

