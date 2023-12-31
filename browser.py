from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import QUrl
print("Imported")

class WebBrowser(QMainWindow):


    def __init__(self, *args, **kwargs):
        super(WebBrowser, self).__init__(*args, **kwargs)
        
        self.window = QWidget()
        self.window.setWindowTitle("Simple Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()


        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("Back")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton("Forward")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        
        self.browser.setUrl(QUrl("http://google.com"))
        self.url_bar.setText("http://google.com")

        self.window.setLayout(self.layout)
        self.window.show()


    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://"+url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

print("defined")
app = QApplication([])
window = WebBrowser()
app.exec_()







