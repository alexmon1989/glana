from modeltranslation.translator import translator, TranslationOptions
from .models import Product, ProductType, ProductProperty, DeliveryPaymentDescription


class ProductTypeOptions(TranslationOptions):
    fields = ('title', )


class ProductOptions(TranslationOptions):
    fields = ('title', 'short_description', 'short_description_2', 'long_description', 'price_description')


class ProductPropertyOptions(TranslationOptions):
    fields = ('title', 'value')


class DeliveryPaymentDescriptionOptions(TranslationOptions):
    fields = ('block_title', 'content')


translator.register(ProductType, ProductTypeOptions)
translator.register(Product, ProductOptions)
translator.register(ProductProperty, ProductPropertyOptions)
translator.register(DeliveryPaymentDescription, DeliveryPaymentDescriptionOptions)
