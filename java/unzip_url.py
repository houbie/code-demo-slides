import pathlib
import sys
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


def main(url, dest):
    if pathlib.Path(dest).exists():
        print(f"{dest} exists, skipping download")
        return
    with urlopen(url) as zip_resp:
        with ZipFile(BytesIO(zip_resp.read())) as zip_file:
            zip_file.extractall(dest)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
