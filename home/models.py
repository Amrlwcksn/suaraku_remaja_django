from django.db import models

class Subscription(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)  # <-- Pastikan ini ada!
    
    def __str__(self):
        return self.email

