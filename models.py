from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

import ast

class Link(models.Model):
    name = models.CharField(max_length=80, verbose_name="Name")
    link_url = models.URLField(verbose_name="URL")
    description = models.TextField(verbose_name="Description", blank=True, null=True)

    def clean(self):
        try:
            self.clean_fields()
        except ValidationError as e:
            error_dict = ast.literal_eval(str(e))
            user_facing_dict = {}
            for key, verbose_key in zip(['name', 'link_url', 'description'], ['Name', 'URL', 'Description']):
                if key in error_dict:
                    user_facing_dict[verbose_key] = ', '.join(error_dict[key])
            raise ValidationError(" ".join([f"{key}: {value}" for key, value in user_facing_dict.items()]))

    def __str__(self):
        return self.name