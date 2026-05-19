import socket
import wx
import wx.grid as gridlib
import os

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Portscanner", size=(450, 350))

        if os.path.exists("logo.ico"):
            self.SetIcon(wx.Icon("logo.ico", wx.BITMAP_TYPE_ICO))

        panel = wx.Panel(self)

        main = wx.BoxSizer(wx.VERTICAL)

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

        # ---- Host Bereich ----
        host_box = wx.BoxSizer(wx.HORIZONTAL)
        host_box.Add(wx.StaticText(panel, label="Host:"), 0, wx.ALL | wx.CENTER, 5)
        host_box.Add(self.host, 1, wx.EXPAND | wx.ALL, 5)

        main.Add(host_box, 0, wx.EXPAND | wx.ALL, 5)

        # ---- Checkbox Bereich ----
        box = wx.StaticBox(panel, label="Ports")
        box_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        grid = wx.FlexGridSizer(rows=0, cols=2, vgap=5, hgap=15)

        for name, port in ports:
            cb = wx.CheckBox(panel, label=f"{name} ({port})")
            cb.my_port = port
            self.checkboxes.append(cb)
            grid.Add(cb, 0, wx.ALL, 3)
        
        port_input_box = wx.BoxSizer(wx.HORIZONTAL)
        port_input_box.Add(wx.StaticText(panel, label="Custom Port:"), 0, wx.ALL | wx.CENTER, 5)
        self.port_input = wx.TextCtrl(panel)
        port_input_box.Add(self.port_input, 1, wx.EXPAND | wx.ALL, 5)
        box_sizer.Add(port_input_box, 0, wx.EXPAND | wx.ALL, 5)
        box_sizer.Add(grid, 1, wx.ALL, 5)
        main.Add(box_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        # ---- Button ----
        self.check_btn = wx.Button(panel, label="Check Ports")
        self.check_btn.Bind(wx.EVT_BUTTON, self.check_port)
        main.Add(self.check_btn, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 10)

        # ---- Ergebnis Grid ----
        self.grid = gridlib.Grid(panel)
        self.grid.CreateGrid(0, 3)

        self.grid.SetColLabelValue(0, "Port")
        self.grid.SetColLabelValue(1, "Status")
        self.grid.SetColLabelValue(2, "Host")

        self.grid.SetColSize(0, 70)
        self.grid.SetColSize(1, 100)
        self.grid.SetColSize(2, 150)

        main.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)

        panel.SetSizer(main)
        self.Show()

    def check_port(self, event):

        # Alte Ergebnisse löschen
        if self.grid.GetNumberRows() > 0:
            self.grid.DeleteRows(0, self.grid.GetNumberRows())

        ports = []

        # Checkboxen prüfen
        for cb in self.checkboxes:
            if cb.GetValue():   # <- FIX
                ports.append(cb.my_port)

        # Custom Ports
        for port in self.port_input.GetValue().split(","):
            try:
                p = int(port.strip())
                if p not in ports:
                    ports.append(p)
            except ValueError:
                pass

        host = self.host.GetValue().strip()

        if not host:
            wx.MessageBox("Bitte Host eingeben!", "Fehler")
            return

        close = wx.Colour(255, 180, 180)
        open_c = wx.Colour(180, 255, 180)

        for port in ports:
            try:
                with socket.create_connection((host, port), timeout=5):

                    self.grid.AppendRows(1)
                    row = self.grid.GetNumberRows() - 1

                    self.grid.SetCellValue(row, 0, str(port))
                    self.grid.SetCellValue(row, 1, "Open")
                    self.grid.SetCellBackgroundColour(row, 1, open_c)
                    self.grid.SetCellValue(row, 2, host)

            except Exception:

                self.grid.AppendRows(1)
                row = self.grid.GetNumberRows() - 1

                self.grid.SetCellValue(row, 0, str(port))
                self.grid.SetCellValue(row, 1, "Closed")
                self.grid.SetCellBackgroundColour(row, 1, close)
                self.grid.SetCellValue(row, 2, host)

        self.host.SetValue("")


app = wx.App()
MyFrame()
app.MainLoop()