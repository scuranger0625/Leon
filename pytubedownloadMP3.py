import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QFileDialog, QVBoxLayout, QMessageBox
from pytube import YouTube, Playlist

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle("YouTube Playlist Downloader")

        layout = QVBoxLayout()

        self.url_label = QLabel("Enter YouTube Playlist URL:", self)
        layout.addWidget(self.url_label)

        self.url_input = QLineEdit(self)
        layout.addWidget(self.url_input)

        self.folder_label = QLabel("Select download folder:", self)
        layout.addWidget(self.folder_label)

        self.folder_button = QPushButton('Choose folder', self)
        self.folder_button.clicked.connect(self.showDialog)
        layout.addWidget(self.folder_button)

        self.download_button = QPushButton('Start Download', self)
        self.download_button.clicked.connect(self.download_playlist)
        layout.addWidget(self.download_button)

        self.setLayout(layout)
        self.show()

    def showDialog(self):
        self.target_directory_train = QFileDialog.getExistingDirectory(self, 'Select folder')
        if self.target_directory_train:
            self.folder_label.setText(f"Download folder: {self.target_directory_train}")

    def download_playlist(self):
        playlist_url = self.url_input.text()

        if not playlist_url:
            QMessageBox.warning(self, 'Error', 'Please enter a valid YouTube playlist URL')
            return

        if not self.target_directory_train:
            QMessageBox.warning(self, 'Error', 'Please select a download folder')
            return

        try:
            playlist = Playlist(playlist_url)
            for video_url in playlist.video_urls:
                try:
                    yt = YouTube(video_url)
                    audio_stream = yt.streams.filter(only_audio=True).first()
                    source_path = audio_stream.download(output_path=self.target_directory_train)
                    target_path = os.path.join(self.target_directory_train, f"{yt.title}.mp3")

                    print(f"Audio MP3 downloaded for video '{yt.title}'")

                except Exception as e:
                    print(f"Error downloading MP3 audio for video '{video_url}': {e}")

            QMessageBox.information(self, 'Complete', 'All MP3 audio downloaded to specified folder')

        except Exception as e:
            QMessageBox.critical(self, 'Error', f"Error processing playlist: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
