from pathlib import Path
import shutil
import re
import os
from typing import Pattern, Match

target_path = Path(r"D:\Bulk Image Downloader")

# jpg_regex = re.compile(r"^\d\D{1}\d.*.jpg$")jpg
jpg_regex = re.compile(r"^web.*jpg$")
dir = target_path / "web"


def find_files(reg: Pattern[str])->list[str]:
    matching_files = []
    for file_path in target_path.glob(
        "*.jpg"
    ):  # rglob recursively finds all files and directories
        if file_path.is_file() and jpg_regex.match(file_path.name):
            matching_files.append(file_path)
    print(f"{len(matching_files)=}")
    return matching_files


def move_files(matching_files: list)->None:
    if not dir.is_dir():
        dir.mkdir(parents=True, exist_ok=True)
    print(*matching_files)
    for _ in matching_files:
        shutil.move(_, dir)

def delete_files(matching_files:list[str])->None:
    for _ in matching_files:
        if _.is_file():
            _.unlink()

if __name__ == "__main__":
    files: list = find_files(jpg_regex)
    # delete_files(files)
    move_files(files)
