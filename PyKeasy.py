#PyKeasy Source Code
import webbrowser
import time
import pyscreenshot
import pywhatkit
import os
from PIL import Image
from pytube import YouTube
import qrcode
import smtplib
import ctypes
import openai

try:
    def write(text):
        print(text)
except:
    print("Not A Valid String.")


try:
    def playytvideo(text):
        pywhatkit.playonyt(str(text))
except:
    print("Video Title Not Found On YouTube.")


try:
    def remove(text):
        os.remove(str(text))
except:
    print("Can't Find The File.")

try:
    def openimage(path):
        im = Image.open(str(path))
        im.show()
except:
    print("Path Not Found.")
try:
    def sendwhatsappmsg(phone_number, message):
        pywhatkit.sendwhatmsg(str(phone_number), str(message))
except:
    print("Invalid Phone Number Or String Error.")

try:
    def mail(sender, password, subject, message,receiver):
        pywhatkit.send_mail(str(sender), str(password), str(subject), str(message), str(receiver))
except:
     print("Invalid Operation.")

try:
    def take_screenshot():
        image = pyscreenshot.grab()
        image.show()
except:
    print("Errors Occurred While Taking Screenshot")

try:
    def ytvideodownload():
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download('https://www.youtube.com/watch?v=cdwal5Kw3Fc')
except:
    print("An error has occurred")

try:
    def makeqrcode(some_data, path):
        img = qrcode.make(str(some_data))
        img.save(str(path))
except:
    print("Can't Make The QR Code")

try:
    def mail_login(username, password, subject, body_text):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
except:
    print("Cant Login Into The Mail. Server Error. Please Check Your Internet Connection")

try:
    def send_mail(username, password, receiver, subject, body_text):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        subject = subject
        body = body_text
        message = "subject:{}\n\n{}".format(subject, body)
        server.sendmail(str(username), str(receiver), message)
        print("Sent The Mail Successfully.")
        server.quit()
except:
    print("Cant Login Into The Mail. Server Error. Please Check Your Internet Connection")


try:
    def MessageBox(text, title, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

except:
    print("Some Error Occurred")

try:
    def write(text):
        print(text)
except:
    print("Some Error Occurred.")
try:
    def webopen(url):
        webbrowser.open(str(url))
except:
    print("Some Error Has Occurred.")
try:
    def notify(application_name, path_to_icon,message_box, title, time_out_time_in_seconds, time_to_repeat_in_seconds):
        from plyer import notification
        notification.notify(
            app_name = str(application_name),
            app_icon = str(path_to_icon),
            message = str(message_box),
            title = str(title),
            timeout=time_out_time_in_seconds
        )
        time.sleep(time_to_repeat_in_seconds)
except:
    print("Some Error Occurred.")

try:
    def openfile(file_path, which_type):
        with open(str(file_path), str(which_type)) as file:
            file.read()
            file.write()
except:
    print("Some Error Occurred.")

#Finishing The Project
if __name__ in '__main__':
    pass