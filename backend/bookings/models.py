from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class AvailabilitySlot(models.Model):
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='availability_slots'
    )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('doctor', 'date', 'start_time')
        ordering = ['date', 'start_time']

    def __str__(self):
        return f"{self.doctor} | {self.date} {self.start_time}-{self.end_time}"
