from PIL import ImageGrab
from win32gui import FindWindow, SetForegroundWindow, GetWindowRect, ShowWindow
from win32con import SW_SHOWNOACTIVATE

class WindowCamera(object):
  # Pass the window title e.g. 'Steam'
  # Make sure the window is on your main monitor or you'll get a black screen

  def __init__(self, title):
    self.hwnd = FindWindow(None, title)
    if not self.hwnd:
      raise Exception('Invalid window title')
    
  def show_window(self):
    ShowWindow(self.hwnd, SW_SHOWNOACTIVATE)
    SetForegroundWindow(self.hwnd)

  def grab(self):
    bbox = GetWindowRect(self.hwnd)
    return ImageGrab.grab(bbox)
