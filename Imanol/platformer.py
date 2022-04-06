import arcade
from player import Player
from camera import Camera

class Platformer(arcade.Window):
    def __init__(self):
        super().__init__(600, 400, "Platformer", resizable=True, fullscreen=True)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.player = Player()
        self.camera = Camera(self.player.center_x, self.player.center_y, self.width, self.height)
       

        self.map = arcade.load_tilemap("map.tmj")
        self.ground = self.map.sprite_lists["Capa de patrones 1"]
        self.water = self.map.sprite_lists["Tile Layer 2"]
        self.obstacle = self.map.sprite_lists["Tile Layer 3"]
        self.spikes = self.map.sprite_lists["Tile Layer 4"]
        self.bouncer = self.map.sprite_lists["Tile Layer 5"]
        for obstacle in self.obstacle:
            obstacle.change_angle = 1
            obstacle.center_y += 5
        self.bouncerflat = arcade.load_texture("PNG\Tiles\platformPack_tile054.png")
        self.physics = arcade.PhysicsEnginePlatformer(self.player, self.ground)

    def on_draw(self):
        arcade.set_viewport(*self.camera.get_coordinates())
        arcade.start_render()
        self.player.draw()
        self.ground.draw()
        self.water.draw()
        self.obstacle.draw()
        self.spikes.draw()
        self.bouncer.draw()


        
    def on_update(self, delta_time):
        self.physics.update()
        self.obstacle.update()
        if self.player.center_y < -200:
            self.player.left=200
            self.player.bottom=350
        self.player.update_animation(self.physics.can_jump())

        self.camera.x = self.player.center_x
        self.camera.y = self.player.center_y
        collisions = self.player.collides_with_list(self.obstacle)
        for Player in collisions:
            self.player.left = 200
            self.player.bottom = 350
        collisions2 = self.player.collides_with_list(self.spikes)
        for Player in collisions2:    
            self.player.left = 200
            self.player.bottom = 350
        watercollision = self.player.collides_with_list(self.water)
        for Player in watercollision:    
            self.player.change_y += 4
        bouncercollision = self.player.collides_with_list(self.bouncer)
        for Player in bouncercollision:
            self.player.change_y += 5
            self.bouncer.texture = self.bouncerflat




    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player.change_x = 4
        if symbol == arcade.key.A:
            self.player.change_x = -4
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 4
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = -4
        if symbol == arcade.key.SPACE:
            self.physics.jump(10)
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.D:
            self.player.change_x = 0
        if symbol == arcade.key.A:
            self.player.change_x = 0
        if symbol == arcade.key.LEFT:
            self.player.change_angle = 0
        if symbol == arcade.key.RIGHT:
            self.player.change_angle = 0