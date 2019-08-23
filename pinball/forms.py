from django import forms
from django.forms import inlineformset_factory, ModelForm, HiddenInput
from .models import Repair, Pinball, PinballInstance, Location, Company
from datetime import datetime    






class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('pinball', 'symptom', 'repair','id',)
        date_logged = forms.DateTimeField(initial=datetime.now(), required=False)
        exclude = ('id', 'date_logged',)

class AddPinballForm(forms.ModelForm):
    class Meta:
        model=Pinball
        fields= ('title', 'company', 'release', 'summary', 'genre', 'game_series', 'coils', 'parts')

class AddCompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields= ('company_name',)


class AddLocationForm(forms.ModelForm):

    class Meta:
        model=Location
        fields=('name', 'short', 'address',)

class AddPinballInstanceForm(forms.ModelForm):
    class Meta:
        model=PinballInstance
        fields = ('pinball', 'sn', 'location', 'region', 'issues', 'last_PM', 'cabinet', 'status')
        exclude = ('pinball', 'sn', 'region', 'cabinet', 'id')