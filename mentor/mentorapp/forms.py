from django import forms
from mentorapp.models import Student, Mentor, TestModel


class StudentForm(forms.ModelForm) :
    firstname = forms.CharField(max_length=128,)
    lastname = forms.CharField(max_length=128,)
    username = forms.CharField(max_length=50,)
    password = forms.CharField(widget=forms.PasswordInput,)
    confirmPassword = forms.CharField(widget=forms.PasswordInput,)
    email = forms.EmailField(max_length=254,)

    isAStudent = forms.BooleanField()


    aboutYourself = forms.CharField(max_length=500,widget=forms.Textarea)
    #github = models.URLField()
    #website = models.URLField()


    class Meta:
        # Provide an association between the ModelForm and a model
        model = Student
        fields = ('firstname','lastname','username','password','confirmPassword','email','isAStudent','aboutYourself')
        exclude = ('usersince',)


class MentorForm(forms.ModelForm) :
    firstname = forms.CharField(max_length=128,)
    lastname = forms.CharField(max_length=128,)
    username = forms.CharField(max_length=50,)
    password = forms.CharField(widget=forms.PasswordInput,)
    confirmPassword = forms.CharField(widget=forms.PasswordInput,)
    email = forms.EmailField(max_length=254,)
    github = forms.CharField(max_length=128,)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Mentor
        fields = ('firstname','lastname','username','password','confirmPassword','email','github')
        exclude = ('usersince',)
