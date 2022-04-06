import arcade

class Camera:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def get_coordinates(self):
        left = self.x - self.width/2
        right = self.x + self.width/2
        bottom = self.y - self.height/2
        top = self.y + self.height/2
        return left, right, bottom, top