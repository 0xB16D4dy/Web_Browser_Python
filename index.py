import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        # Navigation Bar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Back Button
        back_btn = QToolButton(self)
        back_icon = QIcon.fromTheme("go-previous", QIcon("icons/back.png"))
        back_btn.setIcon(back_icon)
        back_btn.setStatusTip('Back to previous page')
        back_btn.clicked.connect(self.browser.back)
        navbar.addWidget(back_btn)

        # Forward Button
        forward_btn = QToolButton(self)
        forward_icon = QIcon.fromTheme("go-next", QIcon("icons/forward.png"))
        forward_btn.setIcon(forward_icon)
        forward_btn.setStatusTip('Forward to next page')
        forward_btn.clicked.connect(self.browser.forward)
        navbar.addWidget(forward_btn)

        # Reload Button
        reload_btn = QToolButton(self)
        reload_icon = QIcon.fromTheme(
            "view-refresh", QIcon("icons/reload.png"))
        reload_btn.setIcon(reload_icon)
        reload_btn.setStatusTip('Reload page')
        reload_btn.clicked.connect(self.browser.reload)
        navbar.addWidget(reload_btn)

        # Home Button
        home_btn = QToolButton(self)
        home_icon = QIcon.fromTheme("go-home", QIcon("icons/home.png"))
        home_btn.setIcon(home_icon)
        home_btn.setStatusTip('Go to home page')
        home_btn.clicked.connect(self.navigate_home)
        navbar.addWidget(home_btn)

        # URL Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Search Button
        search_btn = QAction('Search', self)
        search_icon = QIcon.fromTheme("go-search", QIcon("icons/search.png"))
        search_btn.setIcon(search_icon)
        search_btn.setStatusTip('Search the web')
        search_btn.triggered.connect(self.search)
        navbar.addAction(search_btn)

        # Set the central widget
        self.setCentralWidget(self.browser)

        # Status Bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        # Update status bar on link hover
        self.browser.urlChanged.connect(self.update_urlbar)
        self.browser.loadFinished.connect(self.update_title)

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("https")

        self.browser.setUrl(q)

    def update_urlbar(self, q):
        self.url_bar.setText(q.toString())
        self.url_bar.setCursorPosition(0)

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle(title)

    def search(self):
        search_text = self.url_bar.text()
        if search_text and not search_text.startswith("http"):
            search_text = "https://www.google.com/search?q=" + search_text
        q = QUrl(search_text)
        if q.scheme() == "":
            q.setScheme("https")

        self.browser.setUrl(q)


app = QApplication(sys.argv)
QApplication.setApplicationName("Python Browser")
window = Browser()
window.showMaximized()
app.exec_()
