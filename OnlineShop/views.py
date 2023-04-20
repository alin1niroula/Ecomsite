from django.shortcuts import render
from store.models import Product, ReviewRating
from slider.models import Slider

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('created_date')
    sliderdata = Slider.objects.all()

    # Get the reviews
    reviews = None
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context = {
        'products': products,
        'reviews': reviews,
        'slider':sliderdata,
    }
    return render(request, 'home.html', context)