from common.json import ModelEncoder
from .forms import LogInForm


class LogInEncoder(ModelEncoder):
    model = LogInForm
    properties = [
        "username",
        "password",
    ]
