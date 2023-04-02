from django.forms import ModelForm
from website.models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
    
        