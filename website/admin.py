from django.contrib import admin
from .models import Post, GaleriaPhotos, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PhotosInline(admin.StackedInline):
    model = GaleriaPhotos
    extra = 1

class PostAdmin(SummernoteModelAdmin):
    list_display = ('id','title', 'price', 'promocao','data_post',)
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    fieldsets = (
        ('Info Gerais', {
            'fields': ('referencia', 'title', 'content', 'price', 'promocao', 'imagem_post', 'categories', 'tamanho', )
        }),
        ('Tamanhos Polónia', {
            'classes': ('collapse',),
            'fields': (('vendido_3_meses', 'stock_3_meses', 'vendas_3_meses'),
                       ('vendido_6_meses', 'stock_6_meses', 'vendas_6_meses'),
                       ('vendido_9_meses', 'stock_9_meses', 'vendas_9_meses'),
                       ('vendido_12_meses', 'stock_12_meses', 'vendas_12_meses'),
                       ('vendido_18_meses', 'stock_18_meses', 'vendas_18_meses'),
                       ('vendido_2_anos', 'stock_2_anos', 'vendas_2_anos'),
                       ('vendido_3_anos', 'stock_3_anos', 'vendas_3_anos'),
                       ('vendido_4_anos', 'stock_4_anos', 'vendas_4_anos'),
                       ('vendido_5_anos', 'stock_5_anos', 'vendas_5_anos'),
                       ('vendido_6_anos', 'stock_6_anos', 'vendas_6_anos'),
                       ('vendido_7_anos', 'stock_7_anos', 'vendas_7_anos'),
                       ('vendido_8_anos', 'stock_8_anos', 'vendas_8_anos'),
                       ('vendido_9_anos', 'stock_9_anos', 'vendas_9_anos'),
                       ('vendido_10_anos', 'stock_10_anos', 'vendas_10_anos'),
                       ('vendido_11_anos', 'stock_11_anos', 'vendas_11_anos'),
                       ('vendido_12_anos', 'stock_12_anos', 'vendas_12_anos'),
                       ('vendido_13_anos', 'stock_13_anos', 'vendas_13_anos'),
                       ('vendido_14_anos', 'stock_14_anos', 'vendas_14_anos'),),
        }),

        ('Tamanhos China', {
            'classes': ('collapse',),
            'fields': (('vendido_2_3_anos', 'stock_2_3_anos', 'vendas_2_3_anos'),
                       ('vendido_3_4_anos', 'stock_3_4_anos', 'vendas_3_4_anos'),
                       ('vendido_4_5_anos', 'stock_4_5_anos', 'vendas_4_5_anos'),
                       ('vendido_5_6_anos', 'stock_5_6_anos', 'vendas_5_6_anos'),
                       ('vendido_6_7_anos', 'stock_6_7_anos', 'vendas_6_7_anos'),
                       ('vendido_7_8_anos', 'stock_7_8_anos', 'vendas_7_8_anos'),
                       ('vendido_8_9_anos', 'stock_8_9_anos', 'vendas_8_9_anos'),
                       ('vendido_9_10_anos', 'stock_9_10_anos', 'vendas_9_10_anos'),
                       ('vendido_10_11_anos', 'stock_10_11_anos', 'vendas_10_11_anos'),),
        }),
    )
    inlines = [PhotosInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'artigo', 'tratado', 'data_contact')
    list_editable = ['tratado',]


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)