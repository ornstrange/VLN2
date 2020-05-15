from django import forms
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from cart.models import Contact_info, Payment_info, Order

def valid_card_num(value):
    if len(value) == 19:
        value = value.replace('-', '')
    if len(value) != 16 or not value.isnumeric():
        raise ValidationError(
            _(f'{value} is not a valid card number'),
            params={'value': value})

def valid_ccv(value):
    if len(value) != 3 or not value.isnumeric():
        raise ValidationError(
            -(f'{value} is not a valid ccv number'),
            params={'value': value}
        )

class Contact_info_form(forms.ModelForm):
    first_name = forms.CharField(max_length=64,
                                 label='First name',
                                 required=True)
    last_name = forms.CharField(max_length=64,
                                label='Last name',
                                required=True)
    country = CountryField(blank_label='Select country').formfield()
    address = forms.CharField(max_length=128,
                             label='Street name and number',
                             required=True)
    city = forms.CharField(max_length=128,
                             label='City name',
                             required=True)
    postcode = forms.CharField(max_length=10,
                             label='Postcode',
                             required=True)

    class Meta:
        model = Contact_info
        fields = ('first_name', 'last_name', 'country',
                  'address', 'city', 'postcode')

class Payment_info_form(forms.ModelForm):
    cardholder = forms.CharField(max_length=128,
                                 required=True,
                                 label='Full cardholder name')
    card_number = forms.CharField(max_length=19,
                                  required=True,
                                  label='Card Number',
                                  validators=[valid_card_num])
    ccv = forms.CharField(max_length=3,
                          required=True,
                          label='Secret code (ccv)',
                          validators=[valid_ccv])
    expiration = forms.DateField(required=True,
                                 label='Expiration date',
                                 help_text='mm/yy or mm/yyyy',
                                 input_formats=['%m/%y', '%m/%Y'])

    class Meta:
        model = Payment_info
        fields = ('cardholder', 'expiration')

    def save(self, commit=True):
        payment_info = super().save(commit=False)
        payment_info.last_four = self.cleaned_data['card_number'][-4:]
        if commit:
            payment_info.save()
        return payment_info

