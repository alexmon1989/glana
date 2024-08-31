import random
import string
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .models import Product


def get_products_upload_to_folder(instance: 'Product', filename: str) -> str:
    return '/'.join(['products', ''.join(random.choices(string.ascii_uppercase + string.digits, k=2)), filename])
