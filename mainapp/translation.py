from modeltranslation.translator import translator, TranslationOptions
from .models import Menu, Slider, SubMenu, Context, Personal
from .models import ArticleContext, Gallery, Images


class MenuTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'data',)


class SliderTranslationOptions(TranslationOptions):
    fields = ('slider_text',)


class SubMenuTranslationOptions(TranslationOptions):
    fields = ('slug', 'title', 'title2', 'title3',
              'data', 'data2', 'data3',)


class ContextTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'title3', 'title4',
              'text', 'text2',)


class PersonalTranslationOptions(TranslationOptions):
    fields = ('name', 'prof', 'info')


class ArticleContextTranslationOptions(TranslationOptions):
    fields = ('title', 'title2', 'title3', 'title4',
              'text1', 'text2', 'text3', 'text4', 'text5',)


# class GalleryTranslationOptions(TranslationOptions):
#     fields = ('text',)
#
#
# class ImagesTranslationOptions(TranslationOptions):
#     fields = ('image_text',)

translator.register(Menu, MenuTranslationOptions)
translator.register(Slider, SliderTranslationOptions)
translator.register(SubMenu, SubMenuTranslationOptions)
translator.register(Context, ContextTranslationOptions)
translator.register(Personal, PersonalTranslationOptions)
translator.register(ArticleContext, ArticleContextTranslationOptions)
# translator.register(Gallery, GalleryTranslationOptions)
# translator.register(Images, ImagesTranslationOptions)
