from django.shortcuts import render
from .models import Genre, ProductData
from django.views.generic import ListView


from django.http.response import HttpResponse
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})

def show_genres2(request):
    return render(request, "home.html", {'genres': Genre.objects.all()})


class HomeView(ListView):
    model = ProductData
    template_name = 'home.html'
    # ordering = ['-publication_date']


    def get_context_data(self, *args, **kwargs): 
         genre_menu = Genre.objects.all()
         context = super(HomeView, self).get_context_data(*args, **kwargs)
         context["genre_menu"] = genre_menu
         return context

    def show_genres2(request):
         return render(request, "home.html", {'genres': Genre.objects.all()})


#this is the view from the blog site
def CategoryView(request, genrep):
    genre_products = ProductData.objects.filter(genre=genrep.replace('-', ' '))
    return render(request, 'categories.html', {'genrep': genrep.replace('-', ' '), 'genre_products': genre_products})












