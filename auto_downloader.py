import os
import pyautogui
import time

print(os.getcwd())

pyautogui.FAILSAFE = False

# Image file paths
launcher_download_path = "download_launcher.PNG"
website_download_path = "download_website.PNG"
delete_error_path = "delete_error.PNG"
install_to_staging = "install_to_staging.PNG"
install_to_staging_v2 = "install_to_staging_v2.PNG"
understood = "understood.PNG"
threshold = 0.88

while True:
    try:
        print("Checking for delete-Button")
        delete_error_location = pyautogui.locateOnScreen(delete_error_path, confidence=threshold)

        if delete_error_location is not None:
            # Click on the launcher download button if found
            print("###delete popup found!###") 
            a,b = pyautogui.position()
            pyautogui.click(delete_error_location.left + 5, delete_error_location.top + 5)
            pyautogui.moveTo(a, b)
            time.sleep(3)

    
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("No delete popup found.")    
		    
    try:
        print("Checking for understood-Button")
        understood_location = pyautogui.locateOnScreen(understood, confidence=threshold)

        if understood_location is not None:
            # Click on the launcher download button if found
            print("###understood popup found!###") 
            a,b = pyautogui.position()
            pyautogui.click(understood_location.left + 5, understood_location.top + 5)
            pyautogui.moveTo(a, b)
            time.sleep(3)

    
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("No understood popup found.")    
		
    try:
        print("Checking for staging-Button")
        install_to_staging_location = pyautogui.locateOnScreen(install_to_staging, confidence=threshold)

        if install_to_staging_location is not None:
            # Click on the launcher download button if found
            print("###staging popup found!###") 
            a,b = pyautogui.position()
            pyautogui.click(install_to_staging_location.left + 5, install_to_staging_location.top + 5)
            pyautogui.moveTo(a, b)
            time.sleep(3)


    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("No staging popup found.")    

    try:
        print("Checking for staging v2-Button")
        install_to_staging_location = pyautogui.locateOnScreen(install_to_staging_v2, confidence=threshold)

        if install_to_staging_location is not None:
            # Click on the launcher download button if found
            print("###staging popup found!###") 
            a,b = pyautogui.position()
            pyautogui.click(install_to_staging_location.left + 5, install_to_staging_location.top + 5)
            pyautogui.moveTo(a, b)
            time.sleep(3)


    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("No staging popup found.")


    try:
        print("Checking for Launcher Download Button")
        launcher_location = pyautogui.locateOnScreen(launcher_download_path, confidence=threshold)

        if launcher_location is not None:
            # Click on the launcher download button if found
            print("###launcher download popup found!###") 
            a,b = pyautogui.position()
            pyautogui.click(launcher_location.left + 5, launcher_location.top + 5)
            pyautogui.moveTo(a, b)

        # Introduce a delay before taking the screenshot
        time.sleep(3)
    
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("Image not found. Waiting for the element to appear.")
        time.sleep(3)  # Add a delay before retrying

    try:
        print("Checking for Website Download Button")
        website_location = pyautogui.locateOnScreen(website_download_path, confidence=threshold)

        if website_location is not None:
            # Click on the website download button if found
            print("###slow download button in browser found!###")
            a,b = pyautogui.position()
            pyautogui.click(website_location.left + 5, website_location.top + 5)
            pyautogui.hotkey('ctrl', 'w')
            pyautogui.moveTo(a, b)

        time.sleep(3)
        print("Waiting for 5 seconds...")
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("Image not found. Waiting for the element to appear.")
        time.sleep(3)  # Add a delay before retrying
		
    print("---------------------------------")