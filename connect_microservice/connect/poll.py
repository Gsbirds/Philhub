import json
import requests

from .models import FileVO


def get_conferences():
    # /////////////////////////////////////////////////////////////!!!!!!!!!!
    url = "http://mono4:8000/philhub/searchworks/"
    # mono needs to match container and make sure in allowed hosts!!!!!
    response = requests.get(url)
    content = json.loads(response.content)
    print (content)
    for post in content["posts"]:
        FileVO.objects.update_or_create(
            name= post["name"],
            import_href=post["href"],
            #  author=post["user"]
            # defaults={"name": post["name"]},
        )

        #  next update your papers
        # update favorites?

