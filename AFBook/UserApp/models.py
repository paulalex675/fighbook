from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self, UserName, UserEmail, UserFirstName, UserLastName, DateOfBirth, PhotoFileName, password=None):
        if UserName is None:
            raise TypeError('Users should have a UserName')
        if UserEmail is None:
            raise TypeError('Users should have an Email')

        user = self.model(UserName=UserName, UserEmail=self.normalize_email(UserEmail),
            UserFirstName = UserFirstName, UserLastName = UserLastName, DateOfBirth = DateOfBirth,
            PhotoFileName = PhotoFileName)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, UserName, UserEmail, password=None):
        if password is None:
            raise TypeError('Password should not be None')

        user = self.create_user(self, UserName, UserEmail, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=100, unique=True, db_index=True)
    UserEmail = models.CharField(max_length=100, unique=True, db_index=True)
    UserFirstName = models.CharField(max_length=100)
    UserLastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now =True)

    USERNAME_FIELD = 'UserEmail'
    REQUIRED_FIELDS = ['UserName', 'UserFirstName', 'UserLastName', 'DateOfBirth' ]

    objects = UserManager()

    def __str__(self):
        return self.UserEmail

    def tokens(self):
        return ''
'''

class Styles(models.Model):
    StyleId = models.AutoField(primary_key=True)
    StyleName = models.CharField(max_length=100)
'''