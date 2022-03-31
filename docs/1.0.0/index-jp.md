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
例えば、赤いテキストを出力してみましょう。<br>
このように書けば実現します。
```py
from colorprinttext import cprint
cprint("text","red")
```
## cprint
### text引数
- 