import wx


class ApplicationFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.CreateStatusBar()
        self.SetStatusText("Ok")
