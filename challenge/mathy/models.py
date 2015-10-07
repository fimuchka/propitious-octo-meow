from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Solution(models.Model):
    number = models.PositiveIntegerField()
    sum_squares = models.PositiveIntegerField()
    square_of_sum = models.PositiveIntegerField()
    difference = models.IntegerField()
    occurences = models.PositiveIntegerField(default=1)