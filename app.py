# First things, first. Import the wxPython package.
import wx
from notes_app import ApplicationFrame

# Next, create an application object.
app = wx.App()

# Then a frame.
frm = ApplicationFrame(None, title="Notes App")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
