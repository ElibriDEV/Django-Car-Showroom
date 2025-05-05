from django import forms as f

from posts.models import CommentModel, PostModel


class PostCreationForm(f.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "preview_content", "content", "image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Заголовок"
        self.fields["title"].help_text = ""
        self.fields["title"].widget = f.TextInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["preview_content"].label = "Краткое содержание"
        self.fields["preview_content"].help_text = ""
        self.fields["preview_content"].widget = f.TextInput(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["content"].label = "Основное содержание"
        self.fields["content"].help_text = ""
        self.fields["content"].widget = f.Textarea(
            attrs={
                "class": "form-control",
            }
        )

        self.fields["image"].label = "Изображение"
        self.fields["image"].help_text = ""
        self.fields["image"].widget = f.FileInput(
            attrs={
                "class": "form-control",
                "accept": "image/*",
            }
        )


class CommentCreationForm(f.ModelForm):
    class Meta:
        model = CommentModel
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].label = "Комментарий"
        self.fields["text"].help_text = ""
        self.fields["text"].widget = f.Textarea(
            attrs={
                "placeholder": "Введите комментарий...",
                "class": "form-control",
            }
        )
