from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # events = models.ManyToManyField(Event, related_name='participants')

    def __str__(self):
        return self.name
    



class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name




class Event(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="event"
    )
    # Category class niche likhle double quotation e Category likhte hobe Event class e....

    guests=models.ManyToManyField(Participant, related_name="events")
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        # return f"{self.name} on {self.date}"
        return f"{self.name}"

