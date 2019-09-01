
from django import forms 

class ReservationForm(forms.Form):
    """
    """
    # 
    OPTIONS                     = [("email", "email"),
                                   ("sms", "sms")] 

    #
    number_of_people            = forms.IntegerField()
    date                        = forms.DateField() 
    time                        = forms.TimeField()

    #
    first_name                  = forms.CharField()
    last_name                   = forms.CharField()
    email                       = forms.EmailField(initial = "antho.4@hotmail.fr")
    phone                       = forms.CharField() 
    preferred_communication     = forms.ChoiceField(choices = OPTIONS, widget = forms.RadioSelect())

    # custom validation 
    def clean_email(self, *args, **kwargs):
        """
        """
        email   = self.cleaned_data.get("email")
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("Sorry, but this is not a valid email! Please, don't use \".edu\"")
        return email
