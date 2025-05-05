from django.db import models as m

from logger import LOGGER


class LoggerMixin(m.Model):
    def save(self, **kwargs):
        super().save(**kwargs)
        LOGGER.info("Saved %s(%s)", self.__class__.__name__, self.pk)

    def delete(self, **kwargs):
        super().delete(**kwargs)
        LOGGER.info("Deleted %s(%s)", self.__class__.__name__, self.pk)

    class Meta:
        abstract = True
