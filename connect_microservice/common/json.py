from json import JSONEncoder
from datetime import datetime
from django.db.models import QuerySet
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict
from django.db import models
import json
from django.core import serializers
from django.contrib.auth.models import User

class DateEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            # if o is an instance of datetime
            return o.isoformat()
        else:
            return super().default(o)


class QuerySetEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, QuerySet):
            return list(o)
        else:
            return super().default(o)


class JsonEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, models.Model):
            return model_to_dict(obj)
        if isinstance(obj, QuerySet):
            return serializers.serialize('python', obj, ensure_ascii=False)
        return super(JsonEncoder, self).default(obj)
    def json_encode(user):
        user= User.objects.all()
        return json.dumps(user, cls=JsonEncoder, indent=2, separators=(',', ': '))
    
class ModelEncoder(DateEncoder, QuerySetEncoder, JSONEncoder):
    encoders = {}

    def default(self, o):
        if isinstance(o, self.model):
            d = {}
            if hasattr(o, "get_api_url"):
                d["href"] = o.get_api_url()
            for property in self.properties:
                value = getattr(o, property)
                if property in self.encoders:
                    encoder = self.encoders[property]
                    value = encoder.default(value)
                d[property] = value
            d.update(self.get_extra_data(o))
            return d
        else:
            return super().default(o)

    def get_extra_data(self, o):
        return {}
