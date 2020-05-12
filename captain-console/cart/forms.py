from django import forms
from django_countries.fields import CountryField
from creditcards.models import CardNumberField, CardExpiryField
from cart.models import Contact_info, Payment_info, Order

class Contact_info_form(forms.Form):
    first_name = forms.CharField(max_length=64,
                                 label='First name',
                                 required=True)
    last_name = forms.CharField(max_length=64,
                                label='Last name',
                                required=True)
    country = CountryField(blank_label='Select country')
    street = forms.CharField(max_length=128,
                             label='Street name',
                             required=True)
    city = forms.CharField(max_length=128,
                             label='City name',
                             required=True)
    house_nr = forms.IntegerField(min_value=1,
                                  label='House number',
                                  required=True)
    city = forms.CharField(max_length=10,
                             label='Postcode',
                             required=True)

    class Meta:
        model = Contact_info
        fields = ('first_name', 'last_name', 'country',
                  'street', 'city', 'house_nr', 'postcode')

class Payment_info_form(forms.Form):
    cardholder = forms.CharField(max_length=128,
                                 required=True,
                                 label='Full cardholder name')
    card_number = forms.CharField(max_length=19,
                                  required=True,
                                  label='Card Number')
    ccv = forms.CharField(max_length=3,
                          required=True,
                          label='Secret code (ccv)')
    expiration = forms.DateField(required=True,
                                 label='Expiration date',
                                 input_formats=['%m/%y', '%m/%Y'])

    class Meta:
        model = Payment_info
        fields = ('cardholder', 'expiration')

