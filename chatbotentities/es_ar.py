import re
from .es import ContactParents as BaseContactParent


class ContactParent(BaseContactParent):
    PHONE_NUMBER_REGEX = re.compile(r'(\d{2}[\d\-\(\)\s]{3,}\d{2})', re.VERBOSE | re.IGNORECASE)

