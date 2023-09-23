from django.db import models


class Item(models.Model):

    CHOICES = (
        ('Transport' , 'Transport'),
        ('Food' , 'Food'),
        ('Leisure' , 'Leisure'),
        ('Electronics' , 'Electronics'),
        ('House&Renovation' , 'House&Renovation'),
        ('Cloths' , 'Cloths')
    )

    expense_name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    time_purchased = models.DateTimeField(auto_now=True)
    expense_type = models.CharField(choices=CHOICES , max_length=20)


    def __str__(self):
        return self.expense_name


