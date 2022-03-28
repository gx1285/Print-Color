# color-printtext
![image](https://user-images.githubusercontent.com/78240988/160273481-3bdbedb7-5580-4975-833a-a611bcbc7a8a.png)<br>
![pypivertion](https://img.shields.io/pypi/v/color-printtext.svg)
![pythonvertion](https://img.shields.io/pypi/pyversions/color-printtext.svg)  
[pypi](https://pypi.org/project/color-printtext/)  
[wiki](https://github.com/gx1285/color-printtext/blob/main/docs/index-jp.md)  
printの色を指定するモジュール。<br>
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
サンプルコード
```py
import colorprinttext
colorprinttext.cprint('test','red')
```