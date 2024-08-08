#Automatically organise the files in your downloads folder based on file type.

import os,shutil,platform

def main():
    #This will check what operating system(OS) you use
    if platform.system() == "Windows":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        downloads_path = os.path.expanduser("~/Downloads")

    #This will list the download files
    download_files = os.listdir(downloads_path)
    for file in download_files:
        if os.path.isfile(f"{downloads_path}/{file}"):
            extension = file.split(".")[-1]
            #Invincible file macOS
            #This file is a hidden system file used by macOS to store custom attributes of a folder, such as the position of icons or the choice of a background image.
            if extension == "DS_Store":
                pass
            else:
                try:
                    items = os.listdir(f"{downloads_path}/{extension}")
                except FileNotFoundError:
                    os.makedirs(f"{downloads_path}/{extension}")
                #This will move the files
                finally:
                    shutil.move(f"{downloads_path}/{file}",f"{downloads_path}/{extension}")

if __name__ == "__main__":
    main()


