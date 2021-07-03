from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, GaleriaPhotos, Contact
from django.db.models import Q, Count, Case, When, F
from django.shortcuts import render, redirect


class PostList(ListView):
    template_name = 'post_list.html'
    model = Post
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context.update({
            'items': Post.objects.all().count(),
            'promo': Post.objects.all().order_by('-promocao')[:4],
            'items_promo': Post.objects.filter(promocao__gt=0).count(),
            #ordenar por soma das vendas
            'vendas': Post.objects.annotate(fieldsum = F('vendas_bebe')
                                                     +F('vendas_crianca') + F('vendas_junior')).order_by('-fieldsum')[:4],
            'todos': Post.objects.all().order_by('-data_post')[:4],
        })
        return context


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context.update({
            'items': GaleriaPhotos.objects.filter(post__pk=self.kwargs.get('pk')).count(),
            'todos': GaleriaPhotos.objects.filter(post__pk=self.kwargs.get('pk')),
        })
        return context


def save_form(request, id):
    name = request.POST['name']
    telefone = request.POST['telm']
    email = request.POST['email']
    message = request.POST['message']

    Contact.objects.create(
        name = name,
        telefone = telefone,
        email = email,
        message = message,
        artigo_id = id,
        tratado = False,
    )
    return render(request, 'contact_success.html',{'name':name})




class TodosList(PostList):
    template_name = 'website/todos_list.html'
    # model = Post
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-data_post')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['items'] = Post.objects.all().count()
        return context



class PromoList(PostList):
    template_name = 'website/promo_list.html'
    # model = Post
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(promocao__gt=1).order_by('-promocao')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books

        context.update({
            'promo': Post.objects.filter(promocao__gt=1).order_by('-promocao'),
            'items': Post.objects.filter(promocao__gt=0).count(),
        })
        return context


class BestSalesList(PostList):
    template_name = 'website/bestsales_list.html'
    # model = Post
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(fieldsum = F('vendas_bebe')
                                                     +F('vendas_crianca') + F('vendas_junior')).order_by('-fieldsum')
        return qs
