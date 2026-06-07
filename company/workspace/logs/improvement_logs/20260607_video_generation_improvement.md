# 改善ログ: 動画生成環境の改善

## 役割
ショート動画生成時に見つかった環境上の制約と改善案を記録します。

## 目的
次回以降、より実用的なMP4動画や音声付き動画を安定して作るためです。

## 使い方
動画生成フローを改善するときに参照します。

## 保存先
`company/workspace/logs/improvement_logs/20260607_video_generation_improvement.md`

## 完了条件
制約、原因、改善案、次回確認項目が明記されていること。

# 制約
- ffmpegが通常パスおよびbundled runtimeから見つからなかった。
- MoviePy、imageio-ffmpeg、OpenCVがbundled Pythonに入っていなかった。
- Windows音声合成は声一覧では見えるが、実行時のセキュリティ設定で使用できなかった。

# 対応
- Pillowと手書きAVIライターで、縦型MJPEG AVIを生成した。
- 音声は無音WAVトラックを付与した。
- 投稿用のカバー画像をPNGで別途作成した。

# 次回改善案
- ffmpegを利用可能にして、MP4形式で書き出す。
- 日本語TTSまたは録音ナレーションを用意して、音声付きMP4にする。
- 背景画像素材や生成画像を使い、より動画らしい画作りにする。
- 投稿先別に、YouTubeショート用、TikTok用、Instagramリール用で書き出し設定を分ける。
- 手書きAVIで納品する場合、音声ストリーム付きMJPEGではなく、互換性優先のVideo-only非圧縮DIB AVIを使う。
