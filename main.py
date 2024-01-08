# This is a sample Python script.
import os
import shutil

import numpy as np
from PIL import Image


def clear_git():
    # Clear git directory and create a new one
    print("Clearing git directory")
    shutil.rmtree(".git", ignore_errors=True)
    os.system("git init")
    os.system("git branch -M main2")
    os.system("git remote add origin https://github.com/HiHappyy/GitMessage.git")
    os.system("git config --local user.email drsvnwldn@gmail.com")
    os.system("git config --local user.name HiHappyy")
    os.system("git push origin -d main2")
    print("Git directory cleared")


def git_commit(date):
    # Change a file in the git directory
    with open("README.md", "a") as file:
        # Clear the file and write a random letter
        file.truncate(0)
        content = f"Hello World {date}"
        file.write(content)

    # Create a new git commit
    print("Creating a new git commit")
    os.system("git add .")
    os.system(f'git commit --date="{date} day ago" -m "Added Hello World"')


def git_push():
    # Push the new commit to the remote repository
    print("Pushing the new commit to the remote repository")
    os.system("git push -f -u origin main")
    print("New commit pushed to the remote repository")


def get_message():
    # Open message.png and decode the image to a 2D array
    print("Opening message.png")

    # Open the image using Pillow
    with Image.open("message.png") as img:
        # Convert the image to grayscale (optional, depending on your needs)
        img = img.convert("1")

        # Convert image to a NumPy array
        data = np.array(img)

    return data


if __name__ == '__main__':
    clear_git()

    message = get_message()

    # Set date of top left corner pixel
    date = np.datetime64("2023-12-24")

    # Loop through the 2D array and create a new commit for each pixel
    for i in range(message.shape[1]):
        for j in range(message.shape[0]):
            if not message[j, i]:
                git_commit(date.__str__())
            # Increment the date by one day
            date = np.datetime64(date) + np.timedelta64(1, "D")

    git_push()
