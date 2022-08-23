from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, phonenumber, password=None):
        if not username:
            raise ValueError("Users must have an username")
        if not email:
            raise ValueError("Users must have an email address")
        if not phonenumber:
            raise ValueError("Users must have a phonenumber")    

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            phonenumber = phonenumber
        )    

        user.set_password(password)
        user.save(usinregisterg=self._db)
        return user

    def create_superuser(self, username, email, phonenumber, password):
        user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
            phonenumber=phonenumber,
		)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    





class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phonenumber = models.BigIntegerField(blank=True)
    date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_author = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phonenumber']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_active

    def has_module_perms(self, app_label):
        return True
    