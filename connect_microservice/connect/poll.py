import json
import requests

from .models import FileVO


def get_conferences():
    url = "http://monolith:8000/philhub/searchworks/"
    response = requests.get(url)
    content = json.loads(response.content)
    print (content)
    for post in content:
        FileVO.objects.update_or_create(
            name= post["name"],
            filepath=post["filepath"]
            # defaults={"name": post["name"]},
        )

        #  next update your papers
        # update favorites?