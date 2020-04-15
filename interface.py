import tkinter as tk


class App(tk.Tk):
    """
    Basic app class to initialize everything
    """

    def __init__(self, title: str = None, size: tuple = None) -> None:
        super().__init__()
        self.geometry('{}x{}'.format(size[0], size[1]))
        self.size = size
        self.bind('<Escape>', self.kill)
        self.resizable(False, False)
        self.title(title)

    def kill(self, event):
        self.destroy()

    def add_button(self, side: str = "top", padding: tuple = (20, 20),
                   width: int = 10, text: str = "Button", frame: tk.Frame = None) -> tk.Button:
        if frame is None:
            frame = self
        btn = tk.Button(frame)
        btn['text'] = text
        btn['width'] = width
        btn.pack(side=side, padx=padding[0], pady=padding[1])
        return btn

    def add_label(self, text: str = "label", width: int = 30, frame: tk.Frame = None, side: str = 'top') -> tk.Label:
        if frame is None:
            frame = self
        lbl = tk.Label(frame, anchor='w')
        lbl['text'] = text
        lbl['width'] = width
        lbl.pack(side=side)
        return lbl

    def add_entry(self, frame: tk.Frame = None, initial_text: str = '', side: str = 'top') -> tk.Entry:
        if frame is None:
            frame = self
        entry = tk.Entry(frame)
        entry.insert(0, initial_text)
        entry.pack(side=side, expand=tk.YES, fill=tk.X)
        return entry
