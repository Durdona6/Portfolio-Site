from django.shortcuts import render, redirect
from .forms import ContactForm
from blog.models import Blog,Category
from .models import ContactMe
from about.models import About
from collection.models import Collection

def contactView(request):
    about = About.objects.all()
    category = Category.objects.all()
    collection = Collection.objects.all()
    blog = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    contactMe = ContactMe.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    context = {
        'abouts' : about,
        'form' : form,
        'blogs' : blog,
        'categories' : category,
        'me' : contactMe,
        'collections' : collection,
    }
    return render(request, 'contact.html', context)