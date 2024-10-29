from django.shortcuts import render
from about.models import About
from blog.models import Blog,Category
from .models import Service
from collection.models import Collection
from contact.models import ContactMe



def serviceView(request):
    service = Service.objects.all()
    about =About.objects.all()
    collection = Collection.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    contactme = ContactMe.objects.all()
    context = {
        'abouts' : about,
        'services' : service,
        'me' : contactme,
        'blogs' : blog,
        'categories' : category,
        'collections' : collection,
    }

    return render(request, 'services.html', context)
