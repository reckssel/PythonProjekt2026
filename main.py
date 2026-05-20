import socket
import time
import wx
import wx.grid as gridlib
import os

from style import (
    COLOR_PORT_OPEN, COLOR_PORT_CLOSED,
    WINDOW_SIZE,
    COL_WIDTH_PORT, COL_WIDTH_STATUS, COL_WIDTH_HOST, COL_WIDTH_TIME,
    PADDING_SMALL, PADDING_MEDIUM, PADDING_LARGE,
    DEFAULT_PORTS,
)


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Portscanner", size=WINDOW_SIZE)

        if os.path.exists("logo.ico"):
            self.SetIcon(wx.Icon("logo.ico", wx.BITMAP_TYPE_ICO))

        panel = wx.Panel(self)
        main = wx.BoxSizer(wx.VERTICAL)

        self.host = wx.TextCtrl(panel)
        self.checkboxes = []

        # ---- Host Bereich ----
        host_box = wx.BoxSizer(wx.HORIZONTAL)
        host_box.Add(wx.StaticText(panel, label="Host:"), 0, wx.ALL | wx.CENTER, PADDING_MEDIUM)
        host_box.Add(self.host, 1, wx.EXPAND | wx.ALL, PADDING_MEDIUM)
        main.Add(host_box, 0, wx.EXPAND | wx.ALL, PADDING_MEDIUM)

        # ---- Checkbox Bereich ----
        box = wx.StaticBox(panel, label="Ports")
        box_sizer = wx.StaticBoxSizer(box, wx.VERTICAL)

        grid = wx.FlexGridSizer(rows=0, cols=2, vgap=PADDING_MEDIUM, hgap=15)
        for name, port in DEFAULT_PORTS:
            cb = wx.CheckBox(panel, label=f"{name} ({port})")
            cb.my_port = port
            self.checkboxes.append(cb)
            grid.Add(cb, 0, wx.ALL, PADDING_SMALL)

        port_input_box = wx.BoxSizer(wx.HORIZONTAL)
        port_input_box.Add(wx.StaticText(panel, label="Custom Port:"), 0, wx.ALL | wx.CENTER, PADDING_MEDIUM)
        self.port_input = wx.TextCtrl(panel)
        port_input_box.Add(self.port_input, 1, wx.EXPAND | wx.ALL, PADDING_MEDIUM)

        box_sizer.Add(port_input_box, 0, wx.EXPAND | wx.ALL, PADDING_MEDIUM)
        box_sizer.Add(grid, 1, wx.ALL, PADDING_MEDIUM)
        main.Add(box_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, PADDING_LARGE)

        # ---- Button ----
        self.check_btn = wx.Button(panel, label="Check Ports")
        self.check_btn.Bind(wx.EVT_BUTTON, self.check_port)
        main.Add(self.check_btn, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, PADDING_LARGE)

        # ---- Ergebnis Grid (zentriert) ----
        self.result_grid = gridlib.Grid(panel)
        self.result_grid.CreateGrid(0, 4)
        self.result_grid.SetColLabelValue(0, "Port")
        self.result_grid.SetColLabelValue(1, "Status")
        self.result_grid.SetColLabelValue(2, "Host")
        self.result_grid.SetColLabelValue(3, "Zeit (ms)")
        self.result_grid.SetColSize(0, COL_WIDTH_PORT)
        self.result_grid.SetColSize(1, COL_WIDTH_STATUS)
        self.result_grid.SetColSize(2, COL_WIDTH_HOST)
        self.result_grid.SetColSize(3, COL_WIDTH_TIME)
        self.result_grid.DisableDragRowSize()

        main.Add(self.result_grid, 1, wx.EXPAND | wx.ALL, PADDING_LARGE)

        panel.SetSizer(main)
        self.Show()

    def check_port(self, event):
        # Alte Ergebnisse löschen
        if self.result_grid.GetNumberRows() > 0:
            self.result_grid.DeleteRows(0, self.result_grid.GetNumberRows())

        ports = []

        for cb in self.checkboxes:
            if cb.GetValue():
                ports.append(cb.my_port)

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

        for port in ports:
            self.result_grid.AppendRows(1)
            row = self.result_grid.GetNumberRows() - 1
            self.result_grid.SetCellValue(row, 0, str(port))
            self.result_grid.SetCellValue(row, 2, host)

            start = time.monotonic()
            try:
                with socket.create_connection((host, port), timeout=5):
                    elapsed = int((time.monotonic() - start) * 1000)
                    self.result_grid.SetCellValue(row, 1, "Open")
                    self.result_grid.SetCellBackgroundColour(row, 1, wx.Colour(*COLOR_PORT_OPEN))
                    self.result_grid.SetCellValue(row, 3, f"{elapsed} ms")
            except Exception:
                elapsed = int((time.monotonic() - start) * 1000)
                self.result_grid.SetCellValue(row, 1, "Closed")
                self.result_grid.SetCellBackgroundColour(row, 1, wx.Colour(*COLOR_PORT_CLOSED))
                self.result_grid.SetCellValue(row, 3, f"{elapsed} ms")

        self.host.SetValue("")


app = wx.App()
MyFrame()
app.MainLoop()