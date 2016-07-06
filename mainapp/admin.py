from django.contrib import admin
from .models import Slider, Menu, SubMenu,  Context, Question
from .models import Gallery, Images, Personal, ArticleContext
from modeltranslation.admin import TranslationAdmin




admin.site.register(Question)



class LanguageAdmin(TranslationAdmin):
    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Menu, LanguageAdmin)
admin.site.register(Slider, LanguageAdmin)
admin.site.register(SubMenu, LanguageAdmin)
admin.site.register(Context, LanguageAdmin)
admin.site.register(Personal, LanguageAdmin)





class ImageInline(admin.TabularInline):
    model = Images


class GalleryAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(ArticleContext, LanguageAdmin)
admin.site.register(Gallery, GalleryAdmin)
