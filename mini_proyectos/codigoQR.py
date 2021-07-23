import png
import pyqrcode
from pyqrcode import QRCode

ruta = input("Introduce la URL del código a generar: ")

url = pyqrcode.create(ruta)
url.svg("./mini_proyectos/images/myqr.svg", scale = 8)

url.png("./mini_proyectos/images/myqr.png", scale = 6)



