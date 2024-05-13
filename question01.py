import arcade

class NameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "Welcome, Mark Wolff!")
        self.first_name = None
        self.last_name = None
        self.full_name = "Mark Wolff"
        self.background_color = arcade.color.WHITE

    def setup(self):
        self.first_name = input("First name:Mark ")
        self.last_name = input("Last name:Wolff ")
        self.full_name = f"Welcome, {self.first_name} {self.last_name}!"

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        arcade.draw_text(self.full_name, 100, 200, arcade.color.BLACK, 20)

def main():
    window = NameWindow(400, 300)
    window.setup()
    arcade.run()
if __name__ == "__main__":
    main()
