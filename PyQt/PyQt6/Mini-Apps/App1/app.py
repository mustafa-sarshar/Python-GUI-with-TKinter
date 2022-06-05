import sys
from PyQt6.QtWidgets import QApplication , QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from PyQt6.QtGui import QGuiApplication

class MyApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__()
        uic.loadUi(uifile="app.ui", baseinstance=self)
        
        # self.window_width, self.window_height = 1200, 800
        # self.resize(self.window_width, self.window_height)

        # layout = QVBoxLayout()
        # self.setLayout(layout)

if __name__ == "__main__":
    # Don't auto scale when drag app to a different monitor.
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy())
    
    app = QApplication(sys.argv)
    # app.setStyleSheet("""
    #     QWidget {
    #         font-size: 30px;
    #     }
    # """)
    myapp = MyApp()
    myapp.show()
    
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing window...")