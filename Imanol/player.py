from re import X
import arcade
import time


class Player(arcade.Sprite):
    def __init__(self, left, bottom):
        super().__init__("PNG/Characters/platformChar_idle.png", scale = 0.8)
        self.left = left
        self.bottom = bottom
        self.stand_right_textures =  arcade.load_texture("PNG/Characters/platformChar_idle.png")
        self.walk_right_textures = [
            arcade.load_texture("PNG/Characters/platformChar_walk1.png"),
            arcade.load_texture("PNG/Characters/platformChar_walk2.png")
            ]

        self.direction = "right"
        self.last_texture_change = 0        #last animation update
        self.texture_change_rate = 0.2    #quickness of update
        self.texture_index = -1   #which texture is displayed

        self.jump_right_textures,self.jump_left_textures = arcade.load_texture_pair("PNG/Characters/platformChar_jump.png")

        self.stand_right_textures =  arcade.load_texture_pair("PNG/Characters/platformChar_idle.png")
        walk_right_1, walk_left_1 = arcade.load_texture_pair("PNG/Characters/platformChar_walk1.png")
        walk_right_2, walk_left_2 = arcade.load_texture_pair("PNG/Characters/platformChar_walk2.png")

        self.walk_right_textures = [
             walk_right_1,
             walk_right_2
         ]
        self.walk_left_textures = [
            walk_left_1,
            walk_left_2
         ]


    def update_animation(self, is_touching_ground):
        if self.change_x > 0:
            self.direction = "right"
            if time.time()> self.last_texture_change + self.texture_change_rate:
                self.last_texture_change = time.time()
                self.texture_index +=1
                if self.texture_index >= len(self.walk_right_textures):
                    self.texture_index=0
            
            self.texture = self.walk_right_textures[self.texture_index]
            
            
        if self.change_x == 0:
            if self.direction == "right":
                self.texture = self.stand_right_textures[0]
            if self.direction == "left":
                self.texture = self.stand_right_textures[1]

        if self.change_x < 0:
            self.direction = "left"
            if time.time()> self.last_texture_change + self.texture_change_rate:
                self.last_texture_change = time.time()
                self.texture_index +=1
                if self.texture_index >= len(self.walk_left_textures):
                    self.texture_index=0
            self.texture = self.walk_left_textures[self.texture_index]

        if not is_touching_ground:
            if self.direction == "right":
                self.texture = self.jump_right_textures
            if self.direction == "left":
                self.texture = self.jump_left_textures


