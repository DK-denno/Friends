from django.contrib import admin
from .models import Questions,Answers,Choices,AnsweredQuestion
# Register your models here.

admin.site.register(AnsweredQuestion)
admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Choices)