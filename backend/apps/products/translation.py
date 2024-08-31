from modeltranslation.translator import translator, TranslationOptions
from .models import Product, ProductType


class ProductTypeOptions(TranslationOptions):
    fields = ('title', )


class ProductOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description')


translator.register(ProductType, ProductTypeOptions)
translator.register(Product, ProductOptions)
