import PIL
from PIL import ImageGrab
import io
class CaptureHelper:
    def image_to_byte_array(self, _quality):
        image = ImageGrab.grab()
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, "JPEG", 
                       quality = _quality)
        imgByteArr.seek(0)
        return  imgByteArr.getvalue()