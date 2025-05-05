import django.forms as f
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget

from main.models import FeedBackRequestModel


class FeedBackRequestModelForm(f.ModelForm):
    class Meta:
        model = FeedBackRequestModel
        fields = ["name", "phone"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].help_text = ""
        self.fields["name"].label = "Имя:"
        self.fields["name"].widget = f.TextInput(attrs={"class": "form-control"})

        self.fields["phone"].help_text = ""
        self.fields["phone"].label = "Телефон:"
        self.fields["phone"].widget = RegionalPhoneNumberWidget(region="RU", attrs={"class": "form-control"})
