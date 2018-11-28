from django import forms


class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
    contact_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    content_subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Subject'})
    )
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Message'})
    )
