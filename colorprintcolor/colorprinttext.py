import time

def sleep(value:int):
  """Sleeps the operation for the specified number of seconds.
Added in Ver 0.3"""
  time.sleep(int(value))
  
def vertion(value):
  """Shows the current version.
Added in ver 0.3"""
  print("Color-PrintText Vertion 0.3")
def Redprint(value):
  """Display red text on the console
Added in ver 0.1"""
  RED = '\033[31m'
  END = '\033[0m'
  print(RED + value + END)
def Blueprint(value):
  """Display blue text on the console
Added in ver 0.2"""
  BLUE = '\033[34m'
  END = '\033[0m'
  print(BLUE + value + END)
def Greenprint(value):
  """Display green text on the console
Added in ver 0.2"""
  GREEN = '\033[32m'
  END = '\033[0m'
  print(GREEN + value + END)
def Yellowprint(value):
  """Display yellow text on the console
Added in ver 0.2"""
  YELLOW = '\033[33m'
  END = '\033[0m'
  print(YELLOW + value + END)
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
