from .models import News
from common.json import ModelEncoder
from .models import News


class Show_pageListEncoder(ModelEncoder):
    model = News
    properties = ["title"]
class Show_pageDetailsDetailEncoder(ModelEncoder):
    model = News
    properties = [
        "title",
        "description",
    ]