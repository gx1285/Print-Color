def print(color, value):
  if color == "Green":
    Green = '\033[32m'
    END = '\033[0m'
    print(Green + value + END)
  elif color == "Yellow":
    Yellow = '\033[33m'
    END = '\033[0m'
    print(Yellow + value + END)
  elif color == "Red":
    Red = '\033[31m'
    END = '\033[0m'
    print(Red + value + END)
  elif color == "Blue":
    Blue = '\033[34m'
    END = '\033[0m'
    print(Blue + value + END)
  else:
    Red = '\033[31m'
    END = '\033[0m'
    print(Red + "[Error] The specified color cannot be found." + END)
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
  cutil.SetConsoleAttribute(cutil.stdout_handle, info_.wAttributes)        
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
def Greenwinprint(value):
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

  fg_color = 0x0002 | 0x0008
  cutil.SetConsoleAttribute(cutil.stdout_handle,
                           fg_color | info_.wAttributes & 0x0070)
  print(value)
  cutil.SetConsoleAttribute(cutil.stdout_handle, info_.wAttributes)
def Yellowwinprint(value):
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

  fg_color = 0x0006 | 0x0008
  cutil.SetConsoleAttribute(cutil.stdout_handle,
                           fg_color | info_.wAttributes & 0x0070)
  print(value)
  cutil.SetConsoleAttribute(cutil.stdout_handle, info_.wAttributes)
