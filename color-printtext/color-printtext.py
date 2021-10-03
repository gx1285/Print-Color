def Redprint(value):
  RED = '\033[31m'
  END = '\033[0m'
  print(RED + value + END)
def Blueprint(value):
  BLUE = '\033[34m'
  END = '\033[0m'
  print(RED + value + END)
def REDwinprint(value):
  from ctypes import windll, Structure, byref, wintypes

  class cutil:
      stdout_handle = windll.kernel32.GetStdHandle(-11)
      GetConsoleInfo = windll.kernel32.GetConsoleScreenBufferInfo
      SetConsoleAttribute = windll.kernel32.SetConsoleTextAttribute
 
      class console_screen_buffer_info(Structure):
          _fields_ = [("dwSize", wintypes._COORD),
                      ("dwCursorPosition", wintypes._COORD),
                      ("wAttributes", wintypes.WORD),
                      ("srWindow", wintypes.SMALL_RECT),
                      ("dwMaximumWindowSize", wintypes._COORD)]
 

  info_ = cutil.console_screen_buffer_info()
  cutil.GetConsoleInfo(cutil.stdout_handle, byref(info_))

  fg_color = 0x0004 | 0x0008
  cutil.SetConsoleAttribute(cutil.stdout_handle,
                           fg_color | info_.wAttributes & 0x0070)
def Bluewinprint(value):
  from ctypes import windll, Structure, byref, wintypes

  class cutil:
      stdout_handle = windll.kernel32.GetStdHandle(-11)
      GetConsoleInfo = windll.kernel32.GetConsoleScreenBufferInfo
      SetConsoleAttribute = windll.kernel32.SetConsoleTextAttribute
 
      class console_screen_buffer_info(Structure):
          _fields_ = [("dwSize", wintypes._COORD),
                      ("dwCursorPosition", wintypes._COORD),
                      ("wAttributes", wintypes.WORD),
                      ("srWindow", wintypes.SMALL_RECT),
                      ("dwMaximumWindowSize", wintypes._COORD)]
 

  info_ = cutil.console_screen_buffer_info()
  cutil.GetConsoleInfo(cutil.stdout_handle, byref(info_))

  fg_color = 0x0001 | 0x0008
  cutil.SetConsoleAttribute(cutil.stdout_handle,
                           fg_color | info_.wAttributes & 0x0070)
  print(value)
  cutil.SetConsoleAttribute(cutil.stdout_handle, info_.wAttributes)
