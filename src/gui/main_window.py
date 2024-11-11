# src/gui/main_window.py
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QSlider, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage , QIcon
from core.image_processor import pixelate_image  # This import is correct

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixel Perfect")
        self.setGeometry(100, 100, 800, 600)
        
        #Set Icon
        self.setWindowIcon(QIcon('src/assets/Pxp.png'))


        # Initialize pixel size with a default value
        self.pixel_size = 15

        # Main Widget and Layout
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)

        # Load Image Button
        self.load_button = QPushButton("Load Image", self)
        self.layout.addWidget(self.load_button)
        self.load_button.clicked.connect(self.load_image)

        # Pixelate Image Button
        self.pixelate_button = QPushButton("Pixelate", self)
        self.layout.addWidget(self.pixelate_button)
        self.pixelate_button.clicked.connect(self.pixelate_image)

        # Export Image Button
        self.export_button = QPushButton("Export Image", self)
        self.layout.addWidget(self.export_button)
        self.export_button.clicked.connect(self.export_image)

        # Create a layout for the slider and its label
        self.slider_layout = QHBoxLayout()
        
        # Label for pixel size
        self.pixel_size_label = QLabel(f"Pixel Size: {self.pixel_size}", self)
        self.slider_layout.addWidget(self.pixel_size_label)

        # Slider for Pixel size
        self.pixel_size_slider = QSlider(Qt.Horizontal, self)
        self.pixel_size_slider.setMinimum(1)
        self.pixel_size_slider.setMaximum(50)
        self.pixel_size_slider.setValue(self.pixel_size)  # Default value
        self.pixel_size_slider.setTickInterval(1)  # Tick every 1 step
        self.pixel_size_slider.setTickPosition(QSlider.TicksBelow)  # Show ticks below slider
        self.slider_layout.addWidget(self.pixel_size_slider)
        
        self.layout.addLayout(self.slider_layout)

        # Connect slider value change to the update method
        self.pixel_size_slider.valueChanged.connect(self.update_pixel_size)

        # Image Display label
        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.pixmap = None

    def update_pixel_size(self):
        """Update the pixel size based on the slider's value."""
        self.pixel_size = self.pixel_size_slider.value()
        self.pixel_size_label.setText(f"Pixel Size: {self.pixel_size}")  # Update label text dynamically

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
            pixelated_image = pixelate_image(image, pixel_size=self.pixel_size)

            # Resize the pixelated image to fit within the same size
            self.pixmap = QPixmap.fromImage(pixelated_image).scaled(500, 500, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            # Set the processed image to the label
            self.image_label.setPixmap(self.pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def export_image(self):
        if self.pixmap:
            options = QFileDialog.Options()
            file, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images(*.png *.jpg *.bmp);;All Files (*)", options=options)
            
            if file:
                self.pixmap.save(file)
