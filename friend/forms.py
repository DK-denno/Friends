from django import forms
from .models import Questions,Answers,AnsweredQuestion,Choices

class Questions(forms.ModelForm):
    class Meta:
        model = Questions
        exclude = ['user']
        fields = ['question']

class Choices(forms.ModelForm):
    class Meta:
        model = Choices
        exclude = ['Question']
        fields = ['choiceA','choiceB','choiceC']

