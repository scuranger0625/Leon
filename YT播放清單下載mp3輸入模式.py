import os
from pytube import YouTube, Playlist

# 檢查目標資料夾是否存在，如果不存在，則創建它
target_directory_train = r"C:\Users\Leon\Desktop\python\YTdownload and AIGC\musicdatatrain"
if not os.path.exists(target_directory_train):
    os.mkdir(target_directory_train)
    print("資料夾 'musicdatatrain' 已創建")

# 使用者輸入 YouTube 影片清單 URL
playlist_url = input("請輸入 YouTube 影片清單的 URL：")

try:
    # 創建 Playlist 物件
    playlist = Playlist(playlist_url)

    # 遍歷影片清單中的每個影片 URL
    for video_url in playlist.video_urls:
        try:
            # 創建 YouTube 物件
            yt = YouTube(video_url)

            # 獲取音訊流
            audio_stream = yt.streams.filter(only_audio=True).first()

            # 下載音訊流，並移動到目標資料夾中
            source_path = audio_stream.download(output_path=target_directory_train)
            target_path = os.path.join(target_directory_train, f"{yt.title}.mp3")

            print(f"影片 '{yt.title}' 的 MP3 音訊下載完成")

        except Exception as e:
            print(f"下載影片 '{video_url}' 的 MP3 音訊時出現錯誤：{e}")

    print("所有 MP3 音訊已下載到資料夾 'musicdatatrain'")

except Exception as e:
    print(f"處理影片清單時出現錯誤：{e}")





