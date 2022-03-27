"""
MIT License

Copyright (c) 2022 gx1285

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
ver = "v1.0.0"
import requests
import time
def vertion_check():
    ctp_vertion = requests.get('https://raw.githubusercontent.com/gx1285/color-printtext/main/vertion.txt')
    if f"{ver}\n" != ctp_vertion.text:
        print(f"Latest Version{ctp_vertion.text}has been released.\nYour version is\n{ver}So, it needs to be updated.\nPlease update with pip.")
        return
    print("The latest version is installed.({ver})")
def sleep(value=None):
  """Sleeps the operation for the specified number of seconds.
Added in Ver 1.0"""
  if value == None:
      raise TypeError('The number of seconds of sleep is not specified.')
  elif type(value) == str:
      raise TypeError('an integer is required (got type str)')
  time.sleep(value)

def vertion():
  """Shows the current version.
Added in ver 1.0"""
  print(f"Color-PrintText Vertion {ver}")
