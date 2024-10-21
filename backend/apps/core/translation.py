from modeltranslation.translator import translator, TranslationOptions
from .models import SeoModel


class SeoModelOptions(TranslationOptions):
    fields = ('meta_h1', 'meta_title', 'meta_description', 'meta_keywords')


translator.register(SeoModel, SeoModelOptions)
