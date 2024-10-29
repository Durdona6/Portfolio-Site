from django.shortcuts import render
from blog.models import Blog,Category
from contact.models import ContactMe
from .models import About, Section
from collection.models import Collection

def aboutView(request):
    about = About.objects.all()
    collection = Collection.objects.all()
    section = Section.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    contactme = ContactMe.objects.all()
    context = {
        'abouts' : about,
        'me' : contactme,
        'sections' : section,
        'blogs' : blog,
        'categories' : category,
        'collections' : collection,
    }
    return render(request, 'about.html', context)
