from django import forms
from query_score.models import UserScore


class UserScoreForm(forms.ModelForm):
    class Meta:
        model = UserScore
        fields = '__all__'
