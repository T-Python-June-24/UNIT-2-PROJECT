from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(label="Your Name",max_length=100)
    phone=forms.CharField(label="Your email",max_length=10)
    subject=forms.CharField(label="Subject",max_length=100)
    message=forms.CharField(label="Message",widget=forms.Textarea)
