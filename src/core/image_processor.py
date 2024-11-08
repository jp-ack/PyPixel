# src/core/image_processor.py
from PyQt5.QtGui import QImage, QColor

def pixelate_image(image: QImage, pixel_size: int) -> QImage:
    width = image.width()
    height = image.height()
    pixelated_image = QImage(width, height, QImage.Format_RGB32)
    
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            r_sum, g_sum, b_sum, count = 0, 0, 0, 0
            for dy in range(pixel_size):
                for dx in range(pixel_size):
                    if x + dx < width and y + dy < height:
                        color = QColor(image.pixel(x + dx, y + dy))
                        r_sum += color.red()
                        g_sum += color.green()
                        b_sum += color.blue()
                        count += 1
            r_avg = r_sum // count
            g_avg = g_sum // count
            b_avg = b_sum // count
            for dy in range(pixel_size):
                for dx in range(pixel_size):
                    if x + dx < width and y + dy < height:
                        pixelated_image.setPixel(x + dx, y + dy, QColor(r_avg, g_avg, b_avg).rgb())
    return pixelated_image
