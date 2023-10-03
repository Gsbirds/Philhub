from .models import News
from common.json import ModelEncoder
from .models import News, File, Notes, Author, Topic
from .forms import ContactForm


class AuthorListEncoder(ModelEncoder):
    model = Author
    properties = ["first_name"]


class AuthorDetailEncoder(ModelEncoder):
    model = Author
    properties = ["first_name", "last_name", "id"]


class Show_pageListEncoder(ModelEncoder):
    model = News
    properties = ["title", "description"]


class Show_pageDetailsDetailEncoder(ModelEncoder):
    model = News
    properties = [
        "title",
        "description",
    ]


class WorksListEncoder(ModelEncoder):
    model = File
    properties = ["name", "id"]

    def get_extra_data(self, o):
        return {"author": o.author.first_name, "topic": o.topic.name}


class Show_WorksDetailEncoder(ModelEncoder):
    model = File
    properties = [
        "name",
        "filepath"
        # "favorites",
    ]


class Show_NotesListEncoder(ModelEncoder):
    model = Notes
    properties = ["title", "text_area", "id"]


class Show_NotesDetailEncoder(ModelEncoder):
    model = Notes
    properties = ["title", "text_area", "author"]


class Show_ContactEncoder(ModelEncoder):
    model = ContactForm
    properties = ["first_name", "email_address", "message"]


class TopicEncoder(ModelEncoder):
    model = Topic
    properties = ["name", "id"]
