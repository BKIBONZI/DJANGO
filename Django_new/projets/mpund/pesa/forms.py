from django import forms
from .models import Article, Arriveesc, Partants

class ContactForm(forms.Form) : 
    sujet = forms.CharField(max_length = 100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoye.", required=False)

class SaisiesArvForm(forms.Form) : 
    dater = forms.CharField()
    paysr = forms.CharField()
    viller = forms.CharField()
    numr = forms.CharField()
    noctr = forms.BooleanField(required=False)
    numc = forms.CharField()
    quintc = forms.BooleanField(required=False)
    nomc = forms.CharField()
    prixc = forms.CharField()
    nbptsc = forms.CharField()
    typec = forms.CharField()
    distc = forms.CharField()
    hdepc = forms.CharField()
    arv1c = forms.CharField()
    arv2c = forms.CharField()
    arv3c = forms.CharField()
    arv4c = forms.CharField()
    arv5c = forms.CharField()
    rapms4c = forms.CharField()


class MyForm(forms.Form):
     email = forms.EmailField(required = True)
     name = forms.CharField(required = True)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class ArriveescForm(forms.ModelForm):
    class Meta:
        model = Arriveesc
        fields = '__all__'


class PartantsForm(forms.ModelForm):
    class Meta:
        model = Partants 
        fields = '__all__'
