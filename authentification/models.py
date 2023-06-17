from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
#the class BaseUserManager is used to create a custom user model
#we are inheriting from the BasUserManager class to use the built-in user
# already provided by django to create a custom user model
# we will override the create_user method to create a custom user model
# we will also override the create_superuser method to create a superuser
class CustomUserManager(BaseUserManager):
    #the custom user model will have an email field and a password field
    # the email field will be used to login instead of the username field
    # the username field will be removed
    # the email field will be the unique identifier for the user
    # (**extra_fields) will be used to pass in any extra fields that
    # we want to add to the user model
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        #the set_password method is used to hash the password
        #the password is hashed for security reasons
        #the password is not stored in plain text
        #the set_password method is a built-in method that
        # use the algorithm PBKDF2 to encrypt the password
        user.set_password(password)
        #using=self._db is used to save the user to the database
        
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)



    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='photos', blank=True)
    birthday = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
    class Meta:
        app_label = 'authentification'
        db_table = 'customer_user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['first_name', 'last_name']
    def __str__(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name


    