
## Front End Import
from tkinter import *
from PIL import ImageTk, Image

## Back End Import
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve

import time
import os

##Example Code
import tkinter.messagebox

downloadPath = 'downloaded'

## Button Event
def corePart(event):

    tkinter.messagebox.showinfo('BonoBono Bot', '포로리한테는 땅깡아지를줄꺼야')

    url = str(url_entry.get())
    file_name = str(file_name_entry.get())

    #start the backend part
    baseUrl = "https://ko.savefrom.net/"

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options)
    driver.get(baseUrl)
    time.sleep(3)

    #Enter the link to input tag in savefrom
    link = url

    inputField = driver.find_elements_by_name('sf_url')[1]
    driver.implicitly_wait(1)
    actions = ActionChains(driver).click(inputField).send_keys(link).send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(12)

    #Click The Download

    try:
        pageSource = driver.page_source
        bs = BeautifulSoup(pageSource, 'html.parser')
        video_url = bs.findAll('a', {'class': 'download-icon'})[0]['href']
    except IndexError as e:
        tkinter.messagebox.showerror('Result', '[-]Download Is fail...! Please Try It Again: {}'.format(e))
        driver.quit()
    else:
        #Set The Path
        path = 'downloaded'
        if not os.path.exists(path):
            os.makedirs(path)

        if video_url:
            #Download the File
            urlretrieve(video_url, './downloaded/{}.mp4'.format(file_name))
            #alert Download is success
            tkinter.messagebox.showinfo('Result', '그리고 이제헛소리하지마 임마!')
            driver.quit()
        else:
            tkinter.messagebox.showerror('Result', '[-]Download Is fail...! Please Try It Again...!')
            driver.quit()



###Front End Part
    
root = Tk()
root.title('BonoBono Bot')
root.resizable(False, False)

## Main Image Path
main_image_path = 'main.jpg'

#Set Main Image
main_image = ImageTk.PhotoImage(Image.open(main_image_path))

#Set Main Image Frame
mainImageFrame = Frame(root)

Label(mainImageFrame, image=main_image).grid(row=0, column=0)

mainImageFrame.pack()

#Set URL Frame
urlFrame = Frame(root)
Label(urlFrame, text='URL', font=('Comic Sans MS', 12, 'bold')).grid(row=0, column=0)
url_entry = Entry(urlFrame, width=30, font=('Comic Sans MS', 12, 'bold'))
url_entry.grid(row=1, column=0)

urlFrame.pack()

#Set Name Frame
fileNameFrame = Frame(root)
Label(fileNameFrame, text='Name', font=('Comic Sans MS', 12, 'bold')).grid(row=0, column=0)
file_name_entry = Entry(fileNameFrame, width=30, font=('Comic Sans MS', 12, 'bold'))
file_name_entry.grid(row=1, column=0)

fileNameFrame.pack()

#Set Button Frame
buttonFrame = Frame(root)
download_button = Button(buttonFrame, text='너부리는 내일 나한테 까만돌맹이를 줄거야', font=('Comic Sans MS', 10, 'bold'), width=37, bg='turquoise2', fg='black')
download_button.bind('<Button-1>', corePart)
download_button.grid(row=0, column=0, pady=3)

exit_button = Button(buttonFrame, text='나가기', font=('Comic Sans MS', 10, 'bold'), width=37, command=root.quit, bg='turquoise4', fg='ivory')
exit_button.grid(row=1, column=0)

buttonFrame.pack()

root.mainloop()