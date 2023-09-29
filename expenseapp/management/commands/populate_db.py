import random
from datetime import datetime, timedelta
import pytz

from django.core.management.base import BaseCommand

from expenseapp.models import Item 


class Command(BaseCommand):
    help = "populate DB with Data"
    def add_arguments(self,parser):
        parser.add_argument("--amount", type=int, help="The number of items that should be created.")
    def handle(self, *args, **options):
        types = ['Medicin','Transport','Food','Leisure','House&Renovations','Electronics','Cloths']

        amount = options["amount"] if options["amount"] else 2500

        for i in range(0,amount):
            dt = pytz.utc.localize(datetime.now() - timedelta(days = random.randint(0 , 1825)))
            expense = Item.objects.create(
                expense_name = str(i),
                price = random.randint(500,50000),
                expense_type = random.choice(types)
            )
            expense.time_purchased = dt
            expense.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))

