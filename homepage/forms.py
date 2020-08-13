from django import forms
from homepage.models import Recipe, Author


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    instructions = forms.CharField(max_length=50)
    time_required = forms.CharField(max_length=50)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "Bio", "user"]

    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=240)
#     password = forms.CharField(widget=forms.PasswordInput)