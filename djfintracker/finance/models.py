from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transcation(models.Model):
    TRANSCATION_TYPE=(
        ('income','Income'),
        ('expense','Expense')
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=200)
    amount=models.DecimalField(max_digits=10,decimal_places=2)

    date=models.DateField()
    transcation_type=models.CharField(max_length=10,choices=TRANSCATION_TYPE)
    category=models.CharField(max_length=200, choices=TRANSCATION_TYPE)