
from common.json import ModelEncoder
from .models import Profile


class Show_profileEncoder(ModelEncoder):
    model = Profile
    properties = ["name"]