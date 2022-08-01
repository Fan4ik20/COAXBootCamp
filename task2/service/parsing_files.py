import requests

import exc

from my_types import video, link

from service.stuff import save_file


def get_video(url: link) -> video:
    try:
        response = requests.get(url, allow_redirects=True)
    except (requests.Timeout, requests.ConnectionError):
        raise exc.CantDownloadVideo

    if response.status_code != 200:
        raise exc.CantDownloadVideo

    return response.content


def get_video_and_save(url: link, directory: str, video_name: str) -> None:
    video_file = get_video(url)

    save_file(video_file, directory, video_name)
