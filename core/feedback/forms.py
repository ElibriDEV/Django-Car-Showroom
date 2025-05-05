from django import forms as f

from feedback.models import FeedbackModel


class FeedbackCreationForm(f.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ["username", "email", "usability", "design", "wishes", "newsletter"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Ваше имя"
        self.fields["username"].help_text = ""
        self.fields["username"].widget = f.TextInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["email"].label = "Ваша почта"
        self.fields["email"].help_text = ""
        self.fields["email"].widget = f.EmailInput(
            attrs={
                "class": "form-control",
            }
        )

        USABILITY_CHOICES = tuple(((str(value + 1), value + 1) for value in range(5)))
        self.fields["usability"].label = "Удобство пользования сайтом"
        self.fields["usability"].help_text = ""
        self.fields["usability"].widget = f.Select(
            choices=USABILITY_CHOICES
        )

        DESIGN_CHOICES = tuple(((str(value + 1), value + 1) for value in range(5)))
        self.fields["design"].label = "Дизайн"
        self.fields["design"].help_text = ""
        self.fields["design"].widget = f.RadioSelect(
            choices=DESIGN_CHOICES
        )

        self.fields["wishes"].label = "Ваши пожелания к сайту"
        self.fields["wishes"].help_text = ""
        self.fields["wishes"].widget = f.Textarea(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["newsletter"].label = "Подписаться на рассылку"
        self.fields["newsletter"].help_text = ""
        self.fields["newsletter"].widget = f.CheckboxInput()
