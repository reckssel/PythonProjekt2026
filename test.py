import wx
import wx.grid as gridlib

def get_data():
    return [
        ["Anna", 25, "Berlin"],
        ["Max", 30, "Hamburg"],
        ["Lisa", 22, "München"]
    ]

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Tabelle Beispiel", size=(400, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        data = get_data()

        grid = gridlib.Grid(panel)
        grid.CreateGrid(len(data), len(data[0]))

        # Spaltenüberschriften
        grid.SetColLabelValue(0, "Name")
        grid.SetColLabelValue(1, "Alter")
        grid.SetColLabelValue(2, "Stadt")

        # Daten füllen
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                grid.SetCellValue(row_idx, col_idx, str(value))

        sizer.Add(grid, 1, wx.EXPAND)
        panel.SetSizer(sizer)

app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()