# src/gui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from core.image_processor import pixelate_image  # This import is correct
  # Import from the core folder

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixelator App")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.load_button = QPushButton("Load Image", self)
        self.layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_image)

        self.pixelate_button = QPushButton("Pixelate", self)
        self.layout.addWidget(self.pixelate_button)
        self.pixelate_button.clicked.connect(self.pixelate_image)

        self.export_button = QPushButton("Export Image", self)
        self.layout.addWidget(self.export_button)
        self.export_button.clicked.connect(self.export_image)


        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.pixmap = None

    def load_image(self):
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file:
            self.pixmap = QPixmap(file)

            # Resize the image to fit within the window size or custom size (e.g., 500x500)
            self.pixmap = self.pixmap.scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Set the image to the label
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)


    def pixelate_image(self):
        if self.pixmap:
            # Convert QPixmap to QImage to work with pixel data
            image = self.pixmap.toImage()

            # Call the pixelate_image function directly
            pixelated_image = pixelate_image(image, pixel_size=8)

            # Resize the pixelated image to fit within the same size
            self.pixmap = QPixmap.fromImage(pixelated_image).scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Set the processed image to the label
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def export_image(self):
        if self.pixmap:
            options = QFileDialog.Options()
            file, _ = QFileDialog.getSaveFileName(self,"Save Image", "" ,"Images(*.png *.jpg *.bmp);;All Files (*)",options = options)
            
            if file:
                self.pixmap.save(file)