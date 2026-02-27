from django import forms
from shared.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


    def clean_messages(self):
        message = self.cleaned_data.get('message')
        if 'Ottaman empire ' in message:
            raise forms.ValidationError(" unfortunately, we do not accept messages that contain the phrase 'Ottaman empire'. Please remove it and try again.")
        return message    
