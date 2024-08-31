from .models import ContactData


def contacts_get_data() -> ContactData:
    """Возвращает данные для контактной информации."""
    return ContactData.objects.first()
