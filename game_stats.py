class GameStats():
    """Отслеживание статистики игры для Alien Invasion."""
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_setting = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0