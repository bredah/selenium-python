import os
import tempfile
import time

import pytest

from pages.heroku.upload_page import UploadPage


@pytest.fixture(name="upload_page")
def setup_page():
    return UploadPage()


def test_upload_file(upload_page):
    temp_file = __generate_file()

    upload_page.open()
    upload_page.upload(temp_file[0])

    result = upload_page.get_info()

    assert result[0] == "File Uploaded!"
    assert result[1] == temp_file[1]


def __generate_file() -> tuple:
    temp_folder = tempfile.gettempdir()
    file_name = f"{int(time.time())}.txt"
    file_path = os.path.join(temp_folder, file_name)

    with open(file_path, "w", encoding="utf-8") as _:
        pass
    return (file_path, file_name)
