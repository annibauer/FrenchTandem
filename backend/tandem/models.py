from django.db import models

class Message(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('tandem', 'Tandem'),
        ('correction', 'Correction')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    session_id = models.UUIDField(null=True, blank=True)  

    def __str__(self):
        return f"[{self.timestamp:%Y-%m-%d %H:%M}] {self.role}: {self.content[:100]}"