##This can be used to rename your files manually, without using OpenAI or Any other LLM
import os

#Add/Remove extensions from these lists according to your need.
video_formats= ('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.m4v', '.mpg', '.mpeg', '.3gp', '.3g2', '.webm', '.vob', '.ogv', '.ts')
subtitle_formats= ('.srt', '.vtt', '.sbv', '.sub', '.ass/.ssa', '.dfxp')


#get the name of media files in a given directory
def findingmedia(directory):
    media=[]
    for path,subdir, files in os.walk(directory):
        for file in files:
            #Appends the path and names of video files into media list.
            if file.lower().endswith(video_formats):
                media.append((path,file))
    return media



#Rename according to inputs provided by the user
def rename(media):
    for element in media:
        #Take input for the new name from user
        print(f'The name of this file is {element[1]}')
        nname=str(input("Enter the new name for this file"))
        try:
            newname= os.path.join(element[0], nname)
            file=os.path.join(element[0], element[1])
            #Rename
            os.rename(file, newname)
        except:
            print(f"Could not rename file {element[1]}")
#Deletes obsolete files other than the files with extensions specified in the subtitle_formats and video_formats tuples.
def deleter(directory):
    count=0
    for path, subdir, files in os.walk(directory):
         for file in files:
            if not file.lower().endswith(subtitle_formats) and not file.lower().endswith(video_formats):
                try:
                    os.remove(os.path.join(path,file))
                    count+=1
                except:
                    print(f"Could not delete file {file}")

def choice():
    choice= input("Do you want to rename any other directory? \n 1. Yes \n 2.No")
    if choice.lower()=='yes' or choice=='1':
        main()
    elif choice.lower()=='no' or choice =='2':
        print("Thank you for using this program :)")
        return
    else:
        print("Wrong input, try again")
        choice()


def main():
    print("Welcome to media renamer ^-^")
    directory=str(input("please enter the directory to be renamed"))
    if not os.path.isdir(directory):
        print("Wrong Directory, exiting")
        choice()
    
    #format=str(input("Please enter the format you will like the files to be renamed in"))
    media=findingmedia(directory)
    if not media:
        print(f"No media files in this directory \n {directory}")
        choice()
    
    rename(media)
    delete= input("Do you want to delete obsolete files in this directory? \n 1. Yes \n 2.No")
    if delete.lower()=='yes' or delete=='1':
        deleter(directory)
        print(f"Files in the directory {directory} renamed and obsolete files deleted successfully.")
        
    elif delete.lower()=='no' or delete=='2':
        print(f"Files in the directory {directory} renamed successfully")
    else:
        print("wrong input, ignoring.")
    choice()

main()
    

    


