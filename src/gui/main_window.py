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

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.pixmap = None

    def load_image(self):
        options = QFileDialog.Options()
        # Set initial directory to 'src' folder (or another folder you want)
        initial_directory = "C:/Users/jp/PixelApp/src"  # Adjust to your folder path
        file, _ = QFileDialog.getOpenFileName(self, "Open Image", initial_directory, "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)
        if file:
            self.pixmap = QPixmap(file)
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)


    def pixelate_image(self):
        if self.pixmap:
            image = self.pixmap.toImage()

            # Call the pixelate_image function from the core module
            pixelated_image = pixelate_image(image, pixel_size=20)

            # Convert back to QPixmap and display
            self.pixmap = QPixmap.fromImage(pixelated_image)
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)
