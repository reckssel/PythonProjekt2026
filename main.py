import socket
import wx

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Portscanner", size=(400,200))

        panel = wx.Panel(self)
        
        grid = wx.FlexGridSizer(rows=10, cols=2, vgap=5, hgap=5)
        ports = [
            ("SSH", 22),
            ("HTTP", 80),
            ("HTTPS", 443),
            ("FTP", 21),
            ("SMTP", 25),
            ("DNS", 53),
            ("IMAP", 143),
            ("POP3", 110),
        ]
        self.host = wx.TextCtrl(panel)
        self.checkboxes = []
        
        
        check = wx.Button(panel, label="Check", pos=(20, 80), size=(100, 30))
        check.Bind(wx.EVT_BUTTON, self.check_port)

        grid.Add(wx.StaticText(panel, label="Host:"), 0, wx.ALL, 5)
        grid.Add(self.host, 0, wx.EXPAND | wx.ALL, 5)

        grid.Add(wx.StaticText(panel, label="Port:"), 0, wx.ALL, 5)
        for name, port in ports:
            cb = wx.CheckBox(panel, label=f"{name} ({port})")
            cb.my_port = port
            self.checkboxes.append(cb)
            grid.Add(cb, 0, wx.ALL, 5)
        

        panel.SetSizer(grid)
        self.Show()
    def check_port(self, event):
        host = self.host.GetValue()
        for cb in self.checkboxes:
            if cb.GetValue():
                port = cb.my_port
                try:
                    with socket.create_connection((host, port), timeout=5) as sock:
                        print(f"Port {port} is open on {host}.")
                except Exception as e:
                    print(f"Port {port} is closed on {host}. Error: {e}")

app = wx.App()
MyFrame()
app.MainLoop()