import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow  # Correctly import from the gui folder

def main():
    app = QApplication(sys.argv)
    window = MainWindow()  # Create the main window
    window.show()  # Show the window
    sys.exit(app.exec_())  # Execute the app

if __name__ == "__main__":
    main()
