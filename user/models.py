from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


""" custom user creation """ 
class CustomUserManager(BaseUserManager):

    """ user creation """ 
    def create_user(self,firstname, lastname, username, email, password, **extra_fields):
        
        # """ ensure firstname is not empty """
        if not firstname:
            raise ValueError(_("Firstname is required"))

        # """ ensure lastname is not empty """
        if not lastname:
            raise ValueError(_("Lastname is required"))

        """ ensure username is not empty """
        if not username:
            raise ValueError(_("Username is required"))

        """ ensure email is not empty """
        if not email:
            raise ValueError(_("Email is required"))

        email = self.normalize_email(email)
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email
            )

        """ ensure password is not empty """
        if password is None:
            raise ValueError(_("Password is required"))

        user.set_password(password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False 
        user.save()

        return user 


    """ super user creation """ 
    def create_superuser(self, firstname, lastname, username, email, password, **extra_fields):

        """ ensure username is not empty """
        if not username:
            raise ValueError(_("Username is required"))

        """ ensure email is not empty """
        if not email:
            raise ValueError(_("Email is required"))

        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=email
            )

        user.is_staff = True 
        user.is_superuser = True 

        """ ensure password is not empty """
        if password is None:
            raise ValueError(_("Password is required"))

        user.set_password(password)
        user.save()

        return user 



""" user model """ 
class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=25, null=False, blank=False)
    lastname = models.CharField(max_length=25, null=False, blank=False)
    username = models.CharField(max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=60, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    """ set username field to username - this allows users login with username and password """ 
    USERNAME_FIELD = "username"
    """ set email as required field """ 
    REQUIRED_FIELDS = ["firstname", "lastname", "email"]

    """ set customusermanger as our user object """ 
    objects = CustomUserManager()

    def __str__(self):
        return self.username


