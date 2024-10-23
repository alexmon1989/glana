from modeltranslation.translator import translator, TranslationOptions
from .models import DeliveryPage



class DeliveryPageOptions(TranslationOptions):
    fields = ('content', 'meta_h1', 'meta_title', 'meta_description', 'meta_keywords')


translator.register(DeliveryPage, DeliveryPageOptions)
