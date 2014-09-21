# Copyright 2014 Daniel Francis
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os

from gi.repository import GdkPixbuf
from gi.repository import Gdk
from gi.repository import Gtk
from gi.repository import GObject

from globals import IMGSIZE, BUNDLE_PATH


class Option(Gtk.Box):
    def __init__(self, option):
        super(Option, self).__init__(orientation=Gtk.Orientation.VERTICAL)

        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
            os.path.join(BUNDLE_PATH, 'images/%s' % option['image']),
            IMGSIZE, IMGSIZE)
        image = Gtk.Image.new_from_pixbuf(pixbuf)
        image.show()
        self.pack_start(image, True, True, 0)
        label = Gtk.Label(option['title'])
        label.show()
        self.pack_start(label, False, True, 0)
        self.show()


class OptionButton(Gtk.Button):
    def __init__(self, option):
        super(OptionButton, self).__init__()
        self.opt = option
        self.option = Option(option)
        self.add(self.option)
        self.unselect()
        self.show()

    def select(self):
        s, color = Gdk.Color.parse('#0000FF')
        self.modify_bg(Gtk.StateType.NORMAL, color)
        GObject.timeout_add(1000, self.unselect)

    def unselect(self):
        s, color = Gdk.Color.parse('#FF0000')
        self.modify_bg(Gtk.StateType.NORMAL, color)