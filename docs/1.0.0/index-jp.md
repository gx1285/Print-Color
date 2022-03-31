# はじめに
## インストール
pipを使用してインストールすることができます。
```sh
python3 -m pip install -U color-printtext
```
Windowsでは、このコマンドでインストールすることができます。
```sh
py -3 -m pip install -U color-printtext
```
PATHが通っている場合は、このコマンドでインストールすることができます。
```sh
pip install -U color-printtext
```
## クイックスタート
----------
例えば、赤いテキストを出力してみましょう。<br>
このように書けば実現します。
```py
from colorprinttext import cprint
cprint("text","red")
```
# APIリファレンス
## cprint(text,color)
**色つきprintを出力する関数**
----------
## text<br>
内容を入力する引数。

## color
色指定をする引数。
## 色一覧
`red`<br>
`nomal`<br>
`translucent`<br>
`special-character`<br>
`underline`<br>
`color-inversion`<br>
`transparency`<br>
`strikethrough`<br>
`special-character2`<br>
`black`<br>
`green`<br>
`ocher`<br>
`blue`<br>
`purple`<br>
`turquoise`<br>
`nomal2`<br>
`black-background`<br>
`red-background`<br>
`turquoise-background`<br>
`white-background`<br>
`purple-background`<br>
`light-blue-background`<br>
`ocher-background`<br>
`green-background`


-------
## version()
**バージョンを確認する関数。**<br>
実行結果: Color-PrintText version v1.0.0

-------
## sleep(seconds:int)
**secondsに指定した秒数停止。**<br>
## seconds
停止する秒数

-------
## version_check()