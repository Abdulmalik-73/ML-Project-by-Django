from django.db import models

class PredictionHistory(models.Model):
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_size = models.FloatField()
    land_size = models.FloatField()
    location = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    year_built = models.IntegerField()
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Prediction - {self.location} - {self.predicted_price}"
