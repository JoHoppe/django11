from django.db import models

# Create your models here.
class MPStrategy(models.Model):
    """able to define different mealplans"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string reprensation of the model"""
        return self.text

class MPDetails(models.Model):
    """add information to the strategy"""
    text = models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)
    strategy= models.ForeignKey(MPStrategy,on_delete=models.CASCADE)


    def __str__(self):
        """return text"""
        return self.text