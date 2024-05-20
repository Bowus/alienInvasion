class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (16, 0, 32)

        # Ship settings
        self.ship_speed = 10
        self.ship_fspeed = 1
        self.ship_bspeed = 3

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 3
        self.bullet_height = 1000
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000