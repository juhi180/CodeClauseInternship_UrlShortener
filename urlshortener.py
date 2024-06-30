from tkinter import *
import pyshorteners
import pyperclip

def urlshort():
    long_url = url.get()
    short_url = pyshorteners.Shortener().tinyurl.short(long_url)
    sortUrl.set(short_url)


def copy():
    short_url = sortUrl.get()
    pyperclip.copy(short_url)
    

root = Tk()
root.title("URL Shortener")
root.geometry("400x300")
root.configure(bg="#f0f0f0")
url = StringVar()
sortUrl = StringVar()

Label(root, text="URL Shortener App", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
Entry(root, textvariable=url, font=("Arial", 14), width=30, bd=2, relief="solid").pack(pady=10)
Button(root, text="Generate Short URL", font=("Arial", 14), bg="#4CAF50", fg="white", command=urlshort).pack(pady=10)
Entry(root, textvariable=sortUrl, font=("Arial", 14), width=30, bd=2, relief="solid").pack(pady=10)
Button(root, text="Copy Short URL", font=("Arial", 14), bg="#008CBA", fg="white", command=copy).pack(pady=10)
root.mainloop()
