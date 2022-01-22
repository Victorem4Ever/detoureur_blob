from app import App
from tkinter import Tk, filedialog


class Detoureur:

    def __init__(self, image):
        self.img = image
        self.image_size = image.size
        self.x, self.y = image.size
        self.blob_size = None

    
    def select_area(self):
        select_app = App(self.img)

        start_pos, stop_pos = select_app.select()
        
        x_start, y_start = start_pos
        x_end, y_end = stop_pos

        x1 = x_start if x_start <= x_end else x_end
        x2 = x_end if x_end >= x_start else x_start

        y1 = y_start if y_start <= y_end else y_end
        y2 = y_end if y_end >= y_start else y_start

        coordonates = []
        for x_ in range(x1, x2+1):
            for y_ in range(y1, y2+1):
                coordonates.append((x_, y_))

        return coordonates


    def erase(self, pixels: list, color: tuple):
        for pixel in pixels:
            self.img.putpixel(pixel, color)

    


    def save(self):
        Tk().withdraw()
        self.path = filedialog.asksaveasfilename()
        if self.path is None:
            return
        self.img.save(self.path)


    def mean(self, pixels: list):
        pixel = pixels.pop()

        mean_r, mean_g, mean_b, trash = self.img.getpixel(pixel)
        for pixel in pixels:
            r, g, b, trash = self.img.getpixel(pixel)
            mean_r += r
            mean_r //= 2

            mean_g += g
            mean_g //= 2

            mean_b += b
            mean_b //= 2
        
        return mean_r, mean_g, mean_b


    def compare(self, area, value:int = 10):
        
        r1, g1, b1 = area

        bg_pixels = []
        self.blob_size = 0

        for x in range(self.x):
            for y in range(self.y):
                pixel = (x,y)
                r, g, b, trash = self.img.getpixel(pixel)

                if not (abs(r-r1) <= value) or not (abs(g-g1) <= value) or not (abs(b-b1) <= value):
                    bg_pixels.append((x,y))


                else:
                    self.blob_size += 1


        self.erase(bg_pixels, (0,0,0))


    def show(self):
        self.img.show()