import socket
from curses import panel
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Portscanner", size=(400,200))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.host = wx.TextCtrl(panel, pos=(20, 20), size=(200, 25))
        self.port = wx.TextCtrl(panel, pos=(20, 20),size=(200, 25))

        check = wx.Button(panel, label="Check", pos=(20, 60))
        check.Bind(wx.EVT_BUTTON, self.check_port)
    def check_port(self, event):
        host = self.host.GetValue()
        port = self.port.GetValue()
        try:
            with socket.create_connection((host, port), timeout=5) as sock:
                print(f"Port {port} is open on {host}.")
        except Exception as e:
            print(f"Port {port} is closed on {host}. Error: {e}")

app = wx.App()
MyFrame()
app.MainLoop()