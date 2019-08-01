from gi import require_version
require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import Images as IMG

class Quote(Gtk.VBox):
    def __init__(self, text, author):
        Gtk.VBox.__init__(self)

        self.text = text
        self.author = author

        self.create_screen()

    def create_screen(self):
        center = Gtk.VBox()

        logo_image = Gtk.Image()
        logo_image.set_from_pixbuf(IMG.quotepix)

        text = Gtk.Label()
        author = Gtk.Label()
        # text.set_label(self.text)
        text.set_label(self.text)
        author.set_text("~ " + self.author + " ~")

        tempdesc = Pango.FontDescription("AnjaliOldLipi Bold 30")
        text.override_font(tempdesc)
        text.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        text.set_line_wrap(True)
        # text.set_justify(Gtk.Justification.CENTER)

        authordesc = Pango.FontDescription("AnjaliOldLipi Bold Italic 20")
        author.override_font(authordesc)
        author.override_color(Gtk.StateFlags.NORMAL, Gdk.RGBA(255, 255, 255, 1.0))
        # author.set_line_wrap(True)

        center.pack_start(logo_image, True, False, 0)
        center.pack_start(text, True, False, 0)
        center.pack_start(author, True, False, 0)
        self.add(center)
