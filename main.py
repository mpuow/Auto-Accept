import pyautogui
from time import sleep

# name of image we are searching for
search_image = 'search.png'

# search duration in minutes, will cancel if time limit reached
max_minutes = 0.5
duration = max_minutes * 12     # 12 searches per minute (1 every 5 seconds)

search_iteration = 0

while True:
    # the accept timer is quite long, so we dont need to search super fast
    # this just adds a small delay, it will always have enough time to click accept if a queue pops
    sleep(5)

    # current search iteration
    search_iteration += 1

    # try to find the image, print status if not found yet
    try:
        # search for the accept button, set x and y
        x, y = pyautogui.locateCenterOnScreen(search_image)
        print('Accept found')

        # click at x and y coordinates
        pyautogui.click(x, y)

        break
    except pyautogui.ImageNotFoundException:
        print("Not found yet")

    # break if time limit reached
    if search_iteration >= duration:
        print("Over time limit - ending program")
        break