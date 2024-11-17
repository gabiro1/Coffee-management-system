from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

# Create your models here.
class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False) # i want that seller might be different to the buyer depend on the restriction they have
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    USER_TYPE_CHOICES =(
        ('Buyer','Buyer'),
        ('Seller','Seller')
    )
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)

class Coffee(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    descriptiom = models.TextField(null=True)
    price = models.DecimalField(max_digits=50, decimal_places=3)
    stock = models.PositiveBigIntegerField()
    image=models.ImageField(upload_to='coffeeImage/')

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    coffee= models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date= models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending..')