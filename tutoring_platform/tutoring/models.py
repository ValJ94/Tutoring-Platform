from django.db import models
from django.utils import timezone
from user import models as usermodels

# Create your models here.


maxCharLength = 128


class TeachingSubject(models.Model):
    title = models.CharField(max_length=maxCharLength)
    subject = models.CharField(max_length=maxCharLength)
    teacher = models.ForeignKey(usermodels.User, on_delete=models.CASCADE, related_name='+')
    DIFFICULTY_CHOICES = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('E', 'Expert'),
    )
    difficulty_level = models.CharField(max_length=3, choices=DIFFICULTY_CHOICES)

    def __str__(self):
        return self.title + " taught by " + self.teacher


class MessageThread(models.Model):
    user = models.ForeignKey(usermodels.User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(usermodels.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

class Message(models.Model):
    messageThread = models.ForeignKey('MessageThread', on_delete=models.CASCADE, blank = True, related_name='+')
    messageSender = models.ForeignKey(usermodels.User, on_delete=models.CASCADE, related_name='+')
    messageReceiver = models.ForeignKey(usermodels.User, on_delete=models.CASCADE, related_name='+')
    content = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    messageRead = models.BooleanField(default=False)

    def __str__(self):
        return "from: " + self.messageSender.username + " to:" + self.messageReceiver.username + " messageRead: " + str(self.messageRead)