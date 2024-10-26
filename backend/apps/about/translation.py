from modeltranslation.translator import translator, TranslationOptions
from .models import AboutPage


class AboutPageOptions(TranslationOptions):
    fields = ('content', 'meta_h1', 'meta_title', 'meta_description', 'meta_keywords')


translator.register(AboutPage, AboutPageOptions)
