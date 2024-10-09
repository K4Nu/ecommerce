from django import forms
from .models import Product

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # This allows selecting multiple files in the widget

class ProductForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
        fields = ['name',"gender", 'price', 'description', 'color', 'size']

    def clean_images(self):
        ALLOWED_EXTENSIONS = ["png", "jpg"]
        images = self.files.getlist("images")  # Get list of uploaded files
        errors = []

        # Validate the number of files
        if len(images) > 5:
            raise forms.ValidationError("You can upload a maximum of 5 images.")

        # Validate file extensions
        for image in images:
            extension = image.name.split('.')[-1].lower()
            if extension not in ALLOWED_EXTENSIONS:
                errors.append(f"File {image.name} has an invalid extension. Allowed extensions are: {', '.join(ALLOWED_EXTENSIONS)}.")

        if errors:
            raise forms.ValidationError(errors)

        return images
