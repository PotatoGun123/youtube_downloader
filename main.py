from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

folder_name=""

def openLocation():
    global folder_name
    folder_name=filedialog.askdirectory()

def downloadVideo():
    choice=quality_options.get()
    video_url = url.get()

    yt = YouTube(video_url)
    #TODO: Error Handling
    if(choice==options[0]):
        select=yt.streams.filter(progressive=True).first() #Highest resolution video

    elif(choice==options[1]):
        select=yt.streams.filter(only_audio=True).first()


    select.download(folder_name)
    downloadStatus.config(text="Download Complete")



root=Tk()
root.title("YouTube Downloader")
root.geometry("500x600")
root.columnconfigure(1,weight=1)

video_url_label=Label(root,text="Copy-paste video url here",font=("roboto",15))
video_url_label.grid()
url_var=StringVar()
url=Entry(root,width=50,textvariable=url_var)
url.grid()

#TODO: Error Handling

save_location = Label(root,text="Select download directory",font=("roboto",15))
save_location.grid()

path_button=Button(root,width=10,bg="teal",fg="white",text="Select Path",command=openLocation)
path_button.grid()
#TODO: Error Warning

quality=Label(root,text="Select Quality",font=("roboto",15))
quality.grid()
options=["Video","Audio Only"]
quality_options=ttk.Combobox(root,values=options)
quality_options.grid()

download_button=Button(root,text="Download",width=10,bg="teal",fg="white",command=downloadVideo)
download_button.grid()

downloadStatus=Label(root,text="Download Not Started",font=("roboto",15))
downloadStatus.grid()


root.mainloop()


