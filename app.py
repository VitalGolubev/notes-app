# First things, first. Import the wxPython package.
import wx
from notes_app import ApplicationFrame
from notes_app.services import NotesService

# Next, create an application object.

app = wx.App()

notes_service = NotesService()
# Then a frame.
frm = ApplicationFrame(notes_service, title="Notes App")

# Show it.
frm.Show()

# Start the event loop.
app.MainLoop()
