
from django import forms 

class ContactForm(forms.Form):
    """
    """
    full_name   = forms.CharField(widget = forms.TextInput(attrs = {"placeholder":"Full name"}))
    email       = forms.EmailField(widget = forms.TextInput(attrs = {"placeholder":"Email"}))
    message     = forms.CharField(widget = forms.Textarea(attrs = {"placeholder":"Message"}))
    
    # custom validation 
    def clean_email(self, *args, **kwargs):
        """
        """
        email   = self.cleaned_data.get("email")
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("Sorry, but this is not a valid email! Please, don't use \".edu\"")
        return email
