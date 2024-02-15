from django import forms
from core.models import Contact

class ContactForm(forms.ModelForm):
    # fullname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=Contact
        fields=("name","email","subject","message",)
        widgets={
            "name":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your name"
            }),
            "email":forms.EmailInput(attrs={
                "class":"form-control",
                "placeholder":"Your Email"
            }),
            "subject":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Subject"
            }),
            "message":forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Your message"
            }),
            
        }

    def clean_email(self):
            email=self.cleaned_data["email"]
            if not "gmail" in email:
                 raise forms.ValidationError("Please enter a valid gmail address")
            return email
    
    # def clean_name(self):
    #      name=self.cleaned_data["name"]
    #      if 
            

