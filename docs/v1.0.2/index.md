# Getting started
## install
It can be installed using pip.
```sh
python3 -m pip install -U color-printtext
```
On Windows, install with this command.
```sh
py -3 -m pip install -U color-printtext
```
If you have passed PATH, you can install it with this command.
```sh
pip install -U color-printtext
```
## Quick Start
For example, let's output red text<br>
Writing it this way will make it happen.
```py
from colorprinttext import cprint
cprint("text","red")
```
# API Reference
## cprint(text,color)
**Function to output colored print**<br>
Added in v1.0.0.

----------
## text<br>
Argument to enter content.

## color
Argument to specify the color.
## Color List
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
**Function to check the version.**<br>
Execution result: Color-PrintText version v1.0.2<br>
Added in v1.0.0.

-------
## sleep(seconds:int)
**Stops for the number of seconds specified in seconds.**<br>
## seconds
Number of seconds to stop<br>
Added in v1.0.0.

-------
## version_check()
**Function to check for version updates.**<br>
Added in v1.0.0.

-------
## vertion_v()
**Versioning function.**
Execution result: v1.0.2<br>
Added in v1.0.1.