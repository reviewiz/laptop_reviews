from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

#User Model
class UserManager(BaseUserManager):
    def create_user(self,email,password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an valid email')

        user = self.model(
            email=email
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    
    ID=models.BigAutoField(primary_key=True)
    #username=models.CharField(max_length=200,unique=True)
    #password=models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        default=None, blank=True, null=True
    )
    is_admin = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_deleted=models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

#1. Replace username with phonenumber
#2. implement delete account scenario - when account is deleted is_deleted is 

class user_details(models.Model):
    gender_choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    ID=models.BigAutoField(primary_key=True)
    users=models.ForeignKey(Users,on_delete=models.CASCADE,related_name='Users',default=17)
    #username=models.CharField(max_length=200,unique=True)
    First_Name=models.CharField(max_length=255)
    Middle_Name=models.CharField(max_length=255,default=None, blank=True, null=True)
    Last_Name=models.CharField(max_length=255)
    date_of_birth = models.DateField()
    Gender=models.CharField(max_length=1,choices=gender_choices)