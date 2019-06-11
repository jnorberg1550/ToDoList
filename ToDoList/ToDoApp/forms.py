from django import forms
from .models import ListType


class ListForm(forms.:ListForm):
    class Meta:
        model=ListType
        fields='__all__'_'
 