import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from pytube import YouTube, Playlist

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle("YouTube Playlist Downloader")
        self.setWindowIcon(QIcon(r"C:\Users\Leon\Desktop\python\icon和圖片\doge.jpg"))

        layout = QVBoxLayout()

        self.url_label = QLabel("請輸入 YouTube 影片清單的 URL：", self)
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        self.folder_label = QLabel("選擇下載資料夾：", self)
        layout.addWidget(self.folder_label)

        self.folder_button = QPushButton('選擇資料夾', self)
        self.folder_button.clicked.connect(self.showDialog)
        layout.addWidget(self.folder_button)

        self.download_button = QPushButton('開始下載', self)
        self.download_button.clicked.connect(self.download_playlist)
        layout.addWidget(self.download_button)

        self.setLayout(layout)
        self.show()

    def showDialog(self):
        self.target_directory_train = QFileDialog.getExistingDirectory(self, '選擇資料夾')
        if self.target_directory_train:
            self.folder_label.setText(f"下載資料夾：{self.target_directory_train}")

    def download_playlist(self):
        playlist_url = self.url_input.text()

        if not playlist_url:
            QMessageBox.warning(self, '錯誤', '請輸入有效的 YouTube 影片清單 URL')
            return

        if not self.target_directory_train:
            QMessageBox.warning(self, '錯誤', '請選擇下載資料夾')
            return

        try:
            playlist = Playlist(playlist_url)
            for video_url in playlist.video_urls:
                try:
                    yt = YouTube(video_url)
                    audio_stream = yt.streams.filter(only_audio=True).first()
                    source_path = audio_stream.download(output_path=self.target_directory_train)
                    target_path = os.path.join(self.target_directory_train, f"{yt.title}.mp3")

                    print(f"影片 '{yt.title}' 的 MP3 音訊下載完成")

                except Exception as e:
                    print(f"下載影片 '{video_url}' 的 MP3 音訊時出現錯誤：{e}")

            QMessageBox.information(self, '完成', '所有 MP3 音訊已下載到指定資料夾')

        except Exception as e:
            QMessageBox.critical(self, '錯誤', f"處理影片清單時出現錯誤：{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
