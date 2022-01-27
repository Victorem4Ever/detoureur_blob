from detoureur import Detoureur
from tkinter import Tk, filedialog
from PIL import Image


if __name__ == "__main__":

    Tk().withdraw()
    path = filedialog.askopenfilename()
    if path is None:
        exit()

    img = Image.open(path)


    detoureur = Detoureur(img)

    blob_area = detoureur.select_area()
    mean_blob = detoureur.mean(blob_area)


    detoureur.compare(mean_blob)
    detoureur.save()

    print(detoureur.blob_size, "pixels de blob")

    detoureur.show()