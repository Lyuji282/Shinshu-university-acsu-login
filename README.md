# Shinshu-university-acsu-login

## 使用用途
このPythonプログラムを使えば、握手に自動でログインし、Wifiを繋げることが出来ます。
毎日図書館などで、握手Wifiを利用している方はぜひお使いください。

## 使い方
まず、`` git clone ``かDownloadで全てのファイルをダウンロードします。

そして``input.json``の中身にIDとPASSWORD、GoogleChromeとchromedriverのパスを指定します。

macユーザーの場合は`` browser_path``の変更は必要ありません。
windowsユーザーの方は、お使いのGoogleChromeの絶対パスを指定してください。

chromedriverは[こちら](https://chromedriver.storage.googleapis.com/index.html?path=2.35/ "chromedirver")からダウンロードすることが出来ます。
mac用とwindows用がありますので、お使いの環境に合わしてダウンロードしてください。

お好きな場所に保存した後、input.jsonの内のchromedriver_pathにパスを割り当ててください。
