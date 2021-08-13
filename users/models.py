from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models
import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email,password=None):
        if not email:
            raise ValueError('User must have an email address')

        user=self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user=self.create_user(email,password=password)
        user.is_superuser=True
        user.is_admin=True
        user.is_active=True
        user.save(using=self._db)
        return user


#--------------------------------------------custom_user----------------------------------------#


class MyUser(AbstractBaseUser):
    uuid=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email=models.EmailField(verbose_name='Email Address', max_length=255, unique=True)

    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    contact_number=models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


