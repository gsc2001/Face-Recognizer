import cv2
from loops import search_loop, save_loop
from interface import App
import tkinter as tk


# initializing camera


def start_search()->None:
    """
    Function to start search
    :return:
    """
    camera = cv2.VideoCapture(0)
    search_loop(camera)
    camera.release()
    cv2.destroyAllWindows()


def start_save(entry: tk.Entry)->None:
    """
    Function to start save
    :param entry: tk.Entry object from where name is to be taken
    :return:
    """
    name = entry.get()
    if name == '':
        return
    camera = cv2.VideoCapture(0)
    save_loop(camera,name)
    camera.release()
    cv2.destroyAllWindows()


def main():
    app = App('Face Recognizer', size=(500, 500))
    detect = app.add_button(text='Detect')
    row = tk.Frame(app)
    row['width'] = 150
    label = app.add_label(text='Enter your name:', width=15, frame=row, side='left')
    label['padx'] = 30
    entry = app.add_entry(frame=row, side='left')
    row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
    save = app.add_button(text='Scan')
    detect['command'] = start_search
    save['command'] = (lambda: start_save(entry))
    # search_loop(camera=camera)
    app.mainloop()


if __name__ == '__main__':
    main()
