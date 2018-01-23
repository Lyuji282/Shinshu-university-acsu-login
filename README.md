# Shinshu-university-acsu-login

## 使用用途
このPythonプログラムを使えば、握手に自動でログインし、Wifiを繋げることが出来ます。
毎日図書館などで、握手Wifiを利用している方はぜひお使いください。

## 使い方
まず、`` git clone ``か``download``で全てのファイルをダウンロードします。

そして``input.json``の中身にIDとPASSWORD、GoogleChromeとchromedriverのパスを指定します。

macユーザーの場合は`` browser_path``の変更は必要ありません。
windowsユーザーの方は、お使いのGoogleChromeの絶対パスを指定してください。

chromedriverは[こちら](https://chromedriver.storage.googleapis.com/index.html?path=2.35/ "chromedirver")からダウンロードすることが出来ます。
mac用とwindows用がありますので、お使いの環境に合わしてダウンロードしてください。

お好きな場所に保存した後、input.jsonの内のchromedriver_pathにパスを割り当ててください。


また、input.jsonのheadlessを0以外の値に変更すると、GUI描写を止めることが可能です。
プラウザが自動で動いていることを確認する必要のない場合は、変更してください。


## Pythonの環境構築
上記の説明はPythonが起動できる環境が構築されていることを前提としています。
Pythonの環境が構築されていない方は、[こちら](https://qiita.com/t2y/items/2a3eb58103e85d8064b6)のサイトなどを参考に[anaconda](https://www.anaconda.com/download/#macos)での構築を推奨します。

また、anacondaでの設定完了後は、``pip install selenium``でseleniumのライブラリーもインストールしてください。
