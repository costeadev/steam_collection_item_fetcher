import tkinter as tk
from tkinter import font
import fetcher

def fetch(*args):
    url = text.get("1.0", "end-1c")
    links = fetcher.get_links(url)

    if not links:
        message.configure(text="Invalid link", fg="red")
    else:
        save_to_file(links)
        message.configure(text="Links saved to links.txt", fg="green")

def save_to_file(links):
    f = open("links.txt", "w")
    for link in links:
        f.write(link + "\n")
    f.close()

root = tk.Tk()
root.geometry("500x200")
root.title("Steam Workshop Item Collection Fetcher")

label = tk.Label(root, text="Input a Steam Workshop URL:")
label.pack(pady=10)

custom_font = font.Font(family="Helvetica", size=10)
text = tk.Text(root, height=1, width=67, font=custom_font)
text.pack(padx=5, pady=10, ipady=5)

button = tk.Button(root, text="Fetch URL", command=fetch)
button.pack(pady=10)

message = tk.Label(root)
message.pack(pady=10)

root.mainloop()
