from django import forms

class Student(forms.Form):
    sname=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField(max_length=100)