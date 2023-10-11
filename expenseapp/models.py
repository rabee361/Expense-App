from django.db import models


class Item(models.Model):

    CHOICES = (
        ('Transport' , 'Transport'),
        ('Food' , 'Food'),
        ('Leisure' , 'Leisure'),
        ('Electronics' , 'Electronics'),
        ('House&Renovation' , 'House&Renovation'),
        ('Cloths' , 'Cloths'),
        ('Medicin' , 'Medicin')
    )

    expense_name = models.CharField(max_length = 100)
    price = models.IntegerField(default=0)
    time_purchased = models.DateTimeField(auto_now_add=True)
    expense_type = models.CharField(choices=CHOICES , max_length=20)


    def __str__(self):
        return f"{self.expense_name} ل.س({self.price})"


class Message(models.Model):
    name = models.CharField(max_length=65)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.email