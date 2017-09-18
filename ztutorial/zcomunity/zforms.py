from django.forms import ModelForm
from zcomunity.models import *

class Form(ModelForm):
    class Meta:
        model = Article
        fields = [ 'name', 'title', 'contents', 'url', 'email' ]