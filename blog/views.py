from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from about.models import About
from contact.models import ContactMe
from collection.models import Collection
from .models import Blog,Category,Tag
from .forms import CommentForm, SubscribeForm

def indexView(request):
    about = About.objects.all()
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
        'categories' : category,
        'blogs' : blog,
        'collections' : collection,

    }
    return render(request, 'index.html', context)


def blogView(request):
    about = About.objects.all()
    collection = Collection.objects.all()
    contactme = ContactMe.objects.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    blog = Blog.objects.all().order_by('-id')
    p = Paginator(blog, 2)
    page = request.GET.get('page')
    blog = p.get_page(page)
    cat = request.GET.get('cat')
    form = SubscribeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('.')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    context = {
        'abouts' : about,
        'me' : contactme,
        'categories' : category,
        'tags' : tag,
        'blogs' : blog,
        'form' : form,
        'collections': collection,       
    }   
    return render(request, 'blog.html', context)




def detailView(request, pk):
    blog1 = Blog.objects.all().order_by('-id')
    cat = request.GET.get('cat')
    if cat:
        blog = blog.filter(category__title__iexact=cat)
    about = About.objects.all()
    collection = Collection.objects.all()
    contactme = ContactMe.objects.all()
    tag = Tag.objects.all()
    category = Category.objects.all()
    blog = Blog.objects.get(id=pk)


    form = CommentForm(request.POST or None)
    if form.is_valid():
        com = form.save(commit=False)
        com.blog = blog
        com.save()
        return redirect('.')
    context = {
        'blog1' :blog1,
        'abouts' : about,
        'blogs' : blog,
        'me' : contactme,
        'categories' : category,
        'tags' : tag,
        'form' : form,
        'collections' : collection,
    }   
    return render(request, 'single.html', context)


