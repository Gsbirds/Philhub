from .models import News
from common.json import ModelEncoder
from .models import News, File


class Show_pageListEncoder(ModelEncoder):
    model = News
    properties = ["title"]
class Show_pageDetailsDetailEncoder(ModelEncoder):
    model = News
    properties = [
        "title",
        "description",
    ]
class WorksListEncoder(ModelEncoder):
    model=File
    properties=[
        "name",
    ]
    # def get_extra_data(self, o):
    #     return {"author": o.author}

class Show_WorksDetailEncoder(ModelEncoder):
    model=File
    properties=[
        "name",
        # "favorites",
    ]