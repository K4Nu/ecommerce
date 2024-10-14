from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.shortcuts import redirect,render,HttpResponse
from .models import Product, ProductImage,TestModel
from .forms import ProductForm

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/add_product.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print("EZZZ")
        product = form.save(commit=False)
        images = self.request.FILES.getlist('images')
        print(images)
        # Get the product object without saving it yet.

        # Optionally, you could add custom logic here, such as setting fields
        # product.user = self.request.user  # Example: Set the user who created the product.

        product.save()  # Save the product instance to the database.

        # If needed, you can also work with related objects after saving the product
        # or perform other actions.

        return super().form_valid(form)


def form_invalid(self, form):
    print("Form is invalid")
    print(form.errors)  # Log any errors
    return super().form_invalid(form)
