import os.path
from .models import ProductImage
from django import forms
from .models import Product,Category,ProductImage
from PIL import Image
from django.conf import settings

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # Allow selecting multiple files

class ProductForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = Product
        fields = ['name', 'gender', 'price', 'description', 'color', 'size']

    def save(self, commit=True):
        product = super().save(commit=commit)
        img_files = self.cleaned_data.get("images")

        if img_files and len(img_files) <= 5:
            for i, img_file in enumerate(img_files):
                # Open the image using PIL
                image = Image.open(img_file)

                # Get the file extension
                file_extension = os.path.splitext(img_file.name)[1]

                # Create a unique image name
                image_name = f'{product.name}_{i+1}{file_extension}'

                # Define the save path relative to the media root
                save_path = os.path.join('product_images', image_name)

                # Full save path within MEDIA_ROOT
                full_save_path = os.path.join(settings.MEDIA_ROOT, save_path)

                # Save the image
                image.save(full_save_path)

                # Create the ProductImage record (assuming you have a ProductImage model)
                ProductImage.objects.create(product=product, image=save_path)

        return product



class ImageForm(forms.Form):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=False)