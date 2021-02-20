from pathlib import Path
import os

fileloc = Path(__file__).parent

def get(url, dir=os.path.join(fileloc, "fromURL"),
        filename="target", ext="pdf"):
    from urllib.request import urlopen
    data = urlopen(url).read()

    if not os.path.exists(dir):
        raise OSError("Target directory does not exist")

    file = f"{filename}.{ext}"
    file = os.path.join(dir, file)

    if not os.path.exists(file):
        open(file, mode='x').close()
    with open(file, mode="wb") as fl:
        fl.write(data)

if __name__ == "__main__":
    ext = input("File extension: ")
    link = input("URL: ")
    filename = input("Filename: ")
    get(link, filename=filename, ext=ext)