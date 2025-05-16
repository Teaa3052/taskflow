from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Todo, TaskList

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TaskListForm(forms.ModelForm):
    shared_with = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label='Podijeli s korisnicima'
    )

    class Meta:
        model = TaskList
        fields = ['name', 'shared_with']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['shared_with'].queryset = User.objects.exclude(id=user.id)
            if self.instance.pk:
                self.fields['shared_with'].initial = self.instance.shared_with.all()


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline', 'list']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['list'].queryset = TaskList.objects.filter(
                Q(user=user) | Q(shared_with=user)
            ).distinct()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Naslov ne smije biti prazan.")
        return cleaned_data
