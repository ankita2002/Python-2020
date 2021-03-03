import os
from win10toast import ToastNotifier
def notification():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier()
    title = "Wanna learn amazing codes"
    message = "follow @code_owl on Instagram"
    icon = "icon.ico"
    length = 30
    toast.show_toast(title, message, icon_path=icon, duration=length)

notification()