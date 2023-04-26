from django.contrib import admin
from tutoring.models import TeachingSubject, MessageThread, Message

# Register your models here.

admin.site.register(TeachingSubject)
admin.site.register(MessageThread)
admin.site.register(Message)


