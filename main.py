import wx
from exp_window import GUI

if __name__ == "__main__":
    application = wx.App()
    view = GUI()
    application.MainLoop()
