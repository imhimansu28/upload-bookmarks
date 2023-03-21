from django import forms
from django.core.validators import FileExtensionValidator


class JSONFileValidator(FileExtensionValidator):
    """
    Validator for JSON files.
    """

    def __init__(self, allowed_extensions=("json",)):
        super().__init__(allowed_extensions)


class BookmarkUploadForm(forms.Form):
    file = forms.FileField(
        validators=[JSONFileValidator()],
        widget=forms.FileInput(attrs={"class": "custom-file-input"}),
    )
