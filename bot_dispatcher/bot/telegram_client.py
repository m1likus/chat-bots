import urllib.request
import os
import json
from dotenv import load_dotenv

load_dotenv()


def makeRequest(method: str, **param) -> dict:
    json_data = json.dumps(param).encode("utf-8")

    request = urllib.request.Request(
        method="POST",
        url=f"{os.getenv('TELEGRAM_BASE_URI')}/{method}",
        data=json_data,
        headers={
            "Content-Type": "application/json",
        },
    )

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        response_json = json.loads(response_body)
        assert response_json["ok"] == True
        return response_json["result"]


def getUpdates(**params) -> dict:
    return makeRequest("getUpdates", **params)


def downloadFile(file_path: str) -> None:
    url = f"{os.getenv('TELEGRAM_FILE_URI')}/{file_path}"
    urllib.request.urlretrieve(url, file_path)


def sendMessage(chat_id: int, text: str, **params) -> dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text, **params)


def getMe() -> dict:
    return makeRequest("getMe")


def get_file(file_id: str) -> dict:
    return makeRequest("getFile", file_id=file_id)


def sendPhoto(chat_id: int, photo: str, **params) -> dict:
    return makeRequest("sendPhoto", chat_id=chat_id, photo=photo, **params)
