from django.forms import ModelForm

from .models import Poll

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question','opt1','opt2','opt3']