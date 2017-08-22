from chatbotentities.extractor import AbstractEntity


class DummyEntity(AbstractEntity):
    def __init__(self, value):
        self.value = value
        
    def __call__(self, sentence, default=None):
        if self.value is None:
            if default is not None:
                return [default]
            return None
        if isinstance(self.value, list):
            return self.value
        return [self.value]
