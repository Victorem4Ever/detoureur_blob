from tkinter import Tk, Canvas
from PIL import ImageTk

class App():

    def __init__(self, img):
        self.start_pos = (0,0)

        self.size = img.size
        self.x, self.y = self.size
        
        self.img = img

        self.stop = False



    def on_move(self, event):
        self.canvas.delete("select_area")
        self.final_pos = (event.x, event.y)
        x, y = self.start_pos
        self.canvas.create_rectangle(x, y, event.x, event.y, tag="select_area", fill="blue", outline="red")



    def on_click(self, event):
        self.start_pos = (event.x, event.y)


    def on_press(self, event):
        self.stop = True
        self.root.destroy()


    def select(self):
        self.create_window()

        while not self.stop:
            self.root.update()

        self.root.quit()
        return self.start_pos, self.final_pos


    def create_window(self):
        self.root = Tk()

        self.root.geometry(str(self.x) + "x" + str(self.y))
        self.root.resizable(False, False)

        self.canvas = Canvas(self.root, width=self.x, height=self.y)
        self.canvas.pack()
        
        self.tk_image = ImageTk.PhotoImage(master=self.canvas, width=self.x, height=self.y, image=self.img)

        self.canvas.create_image(self.x//2, self.y//2, image=self.tk_image)

        self.canvas.bind("<B1-Motion>", self.on_move)
        self.canvas.bind("<Button-1>", self.on_click)
        self.root.bind("<KeyRelease>", self.on_press)