import arcade
import os
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from platformer import Platformer


Platformer()
arcade.run()
