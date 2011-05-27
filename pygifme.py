from PIL import Image
import images2gif

images = [Image.open("hunter1.GIF"), Image.open("hunter2.GIF")]

images2gif.writeGif("out.GIF", images)
