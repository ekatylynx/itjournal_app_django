from django.contrib import admin
from .models import News, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'content', 'created_at', 'updated_at', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'id')
    list_editable = ['is_published', 'category']
    readonly_fields = ('created_at', 'updated_at')
    form = NewsAdminForm

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
