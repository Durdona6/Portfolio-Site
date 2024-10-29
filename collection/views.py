from django.shortcuts import render
from .models import Collection
from blog.models import Blog, Category
from about.models import About
from contact.models import ContactMe

def collectionView(request):
    about =About.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    contactme = ContactMe.objects.all()
    collection = Collection.objects.all()
    context = {
        'abouts' : about,
        'me' : contactme,
        'collections' : collection,
        'blogs' : blog,
        'categories' : category,
    }
    return render(request, 'collection.html', context)
