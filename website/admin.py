from django.contrib import admin
from .models import Post, GaleriaPhotos, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = GaleriaPhotos
    extra = 1

class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'price', 'promocao', 'stock_bebe', 'stock_crianca', 'stock_junior', 'vendas_bebe', 'vendas_crianca', 'vendas_junior','data_post',)
    list_display_links = ('id', 'title')
    list_editable = ['stock_bebe', 'stock_crianca', 'stock_junior', 'vendas_bebe', 'vendas_crianca', 'vendas_junior']
    list_filter = ('title',)
    summernote_fields = ('content',)
    inlines = [PhotosInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','tratado', 'data_contact')


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)