from modeltranslation.translator import translator, TranslationOptions
from .models import ContactData



class ContactDataOptions(TranslationOptions):
    fields = ('address', 'meta_h1', 'meta_title', 'meta_description', 'meta_keywords')


translator.register(ContactData, ContactDataOptions)
