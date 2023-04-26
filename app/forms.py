from django import forms
from app.models import *
TO=list(Topic.objects.all())
class TopicForm(forms.ModelForm):
    # topic_name=forms.CharField()
    class Meta:
        model=Topic
        fields='__all__'
class WebPageForm(forms.ModelForm):
    class Meta:
        model=WebPages
        fields='__all__'
    # topic_name=forms.ChoiceField(choices=TO)
    # name=forms.CharField()
    # age=forms.IntegerField()
    # url=forms.URLField()

class AccessRecordForm(forms.Form):
    name=forms.CharField()
    auther=forms.CharField()
    email=forms.EmailField()
