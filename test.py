import wx
import socket

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Portscanner", size=(400, 250))

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Eingabefelder
        self.host = wx.TextCtrl(panel)
        self.port = wx.TextCtrl(panel)

        # Button
        check = wx.Button(panel, label="Check")
        check.Bind(wx.EVT_BUTTON, self.check_port)

        # Layout (WICHTIG!)
        vbox.Add(wx.StaticText(panel, label="Host:"), 0, wx.ALL, 5)
        vbox.Add(self.host, 0, wx.EXPAND | wx.ALL, 5)

        vbox.Add(wx.StaticText(panel, label="Port:"), 0, wx.ALL, 5)
        vbox.Add(self.port, 0, wx.EXPAND | wx.ALL, 5)

        vbox.Add(check, 0, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(vbox)

        self.Show()

    def check_port(self, event):
        host = self.host.GetValue()
        port = self.port.GetValue()

        try:
            sock = socket.socket()
            sock.settimeout(1)

            if sock.connect_ex((host, int(port))) == 0:
                wx.MessageBox("Port ist offen ✅")
            else:
                wx.MessageBox("Port ist geschlossen ❌")

            sock.close()

        except:
            wx.MessageBox("Fehler bei Eingabe")

app = wx.App()
MyFrame()
app.MainLoop()