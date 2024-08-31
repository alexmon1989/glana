from modeltranslation.translator import translator, TranslationOptions
from .models import PageData


class PageDataOptions(TranslationOptions):
    fields = ('meta_h1', 'meta_title', 'meta_keywords', 'meta_description')


translator.register(PageData, PageDataOptions)
