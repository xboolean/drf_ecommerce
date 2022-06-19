import uuid
from django.db import models
from base.logger import Logger
from django.conf import settings
from sentry_sdk import capture_exception

class CustomModelMetaclass(models.base.ModelBase):
	def __new__(mcs, name, bases, newattrs):
		new_class = super(CustomModelMetaclass, mcs).__new__(mcs, name, bases, newattrs)
		new_class.logger = Logger(
			name=name.lower(),
			level="DEBUG",
			output=f"logs/models/{name.lower()}.log",
			rotation=settings.MODELS_LOGGING_FILE_SIZE,
			format="[{time}][{level}][" + name.upper() + "]{message}"
		)
		return new_class

class BaseModel(models.Model, metaclass=CustomModelMetaclass):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def save(self, *args, **kwargs):
        self.logger.info(f"{self.id} saving...")
        self.logger.debug(f"{self.id} Save method. Args = {args}, Kwargs = {kwargs}")
        try:
            result = super(BaseModel, self).save(*args, **kwargs)
        except Exception as error:
            self.logger.error(f"{self.id} Unhandled Exception on saving. {error.__class__.__name__}: {str(error)}")
            capture_exception(error)
            raise error
        else:
            self.logger.success(f"{self.id} Saving process complete successfully")
            return result