from random import randint, uniform, choices

import pygame

# The code is divided into 4 main sections.
# Section 1: Defining constants.
# Section 2: Defining classes.
# Section 3: Defining functions.
# Section 4: The gameplay loop (and other stuff).

pygame.init()

###############################################################################
# Section 1: Defining constants.
###############################################################################

# Might be useful to do this, but Idk.
SPRITE = pygame.sprite.Sprite
SPRITECOLLIDEANY = pygame.sprite.spritecollideany

# Sets up constants for the window and other stuff.

# Gets the size of the desktop view.
# desktop_sizes[0][0] represents the width of the desktop view in pixels.
# desktop_sizes[0][1] represents the height of the desktop view in pixels.
desktop_sizes = pygame.display.get_desktop_sizes()
# The desktop size is then used to make a window that is 84% the height of the desktop view with
# aspect ratio of 1:1. I did this, so that the game's window is the same size on every computer.
SCREEN_WIDTH, SCREEN_HEIGHT = desktop_sizes[0][1] // 1.1875, desktop_sizes[0][1] // 1.1875

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creates the window for the game.
pygame.display.set_caption("The Maze Generator")

CLOCK = pygame.time.Clock()

# Sets up constants for the maze.

COLUMNS, ROWS = 12, 12

# This ensures that, no matter what COLUMNS or ROWS are equal to, each cell will be square-shaped.
if COLUMNS > ROWS:
    HORIZONTAL_CELL_WIDTH = SCREEN_WIDTH / COLUMNS
    VERTICAL_CELL_HEIGHT = HORIZONTAL_CELL_WIDTH
else:
    VERTICAL_CELL_HEIGHT = SCREEN_HEIGHT / ROWS
    HORIZONTAL_CELL_WIDTH = VERTICAL_CELL_HEIGHT

MAZE_WIDTH = COLUMNS * HORIZONTAL_CELL_WIDTH
MAZE_HEIGHT = ROWS * VERTICAL_CELL_HEIGHT

AVERAGE_CELL_WIDTH = (HORIZONTAL_CELL_WIDTH * VERTICAL_CELL_HEIGHT) ** 0.5

HORIZONTAL_OFFSET = HORIZONTAL_CELL_WIDTH / 2  # Used to properly position things horizontally in a cell.
VERTICAL_OFFSET = VERTICAL_CELL_HEIGHT / 2  # Used to properly position things vertically in a cell.

# Sets the background for all mazes.
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("sprites/background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Sets up constants for the player.

# Sets the player's speeds.
# 1 is added, so that if the rest is 0, then the player will still get some speed.
PLAYER_SPEED_SLOW = 42//((COLUMNS * ROWS) ** 0.5) + 1
PLAYER_SPEED_NORMAL = 56//((COLUMNS * ROWS) ** 0.5) + 1
PLAYER_SPEED_FAST = 70//((COLUMNS * ROWS) ** 0.5) + 1

# Sets the images used for the player.
PLAYER_STATE_FAST_IMAGE = pygame.transform.scale(pygame.image.load("sprites/player/player_state_fast.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
PLAYER_STATE_SLOW_IMAGE = pygame.transform.scale(pygame.image.load("sprites/player/player_state_slow.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
PLAYER_STATE_NORMAL_IMAGE = pygame.transform.scale(pygame.image.load("sprites/player/player_state_normal.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))

# Sets up constants for the powerups.

# Sets the images used for the powerups.
POWERUP_END_IMAGE = pygame.transform.scale(pygame.image.load("sprites/powerup/powerup_end.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
POWERUP_FAST_IMAGE = pygame.transform.scale(pygame.image.load("sprites/powerup/powerup_fast.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
POWERUP_SLOW_IMAGE = pygame.transform.scale(pygame.image.load("sprites/powerup/powerup_slow.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))

# Sets up constants for the enemies.

# Sets the speeds for the enemies.
ENEMY_SPEED_SLOW = 32//((COLUMNS * ROWS) ** 0.5) + 1
ENEMY_SPEED_NORMAL = 42//((COLUMNS * ROWS) ** 0.5) + 1
ENEMY_SPEED_FAST = 53//((COLUMNS * ROWS) ** 0.5) + 1

# Sets the images used for the enemies.

ENEMY_STATE_TYPE_1_FAST_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_1/enemy_state_type_1_fast.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
ENEMY_STATE_TYPE_1_SLOW_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_1/enemy_state_type_1_slow.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
ENEMY_STATE_TYPE_1_NORMAL_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_1/enemy_state_type_1_normal.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))

ENEMY_STATE_TYPE_2_FAST_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_2/enemy_state_type_2_fast.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
ENEMY_STATE_TYPE_2_SLOW_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_2/enemy_state_type_2_slow.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))
ENEMY_STATE_TYPE_2_NORMAL_IMAGE = pygame.transform.scale(pygame.image.load("sprites/enemy/type_2/enemy_state_type_2_normal.png"), (HORIZONTAL_OFFSET, VERTICAL_OFFSET))

# The below list will hold the music that the game will use.
MUSIC = []
# You can add your own music by putting a song in the working directory
# and then putting a string of the song name in the list below.
# The string must also include the file extension.
track_names = []
# Btw, all of the default music below comes from a game called VVVVVV.
# I decided to not include the default music.

# track_names.extend([
#     "Predestined Fate Remixed.mp3",
#     "Paced Energy.mp3",
#     "Passion for Exploring.mp3",
#     "Pressure Cooker.mp3",
#     "Pushing Onwards.mp3"
# ])

for name in track_names:
    # Attempt to find and load in music with the names above.
    try:
        MUSIC.append(pygame.mixer.Sound(f"{name}"))
    # If a track can't be found, then the program will skip it.
    # This is done so that the program doesn't need the music in order to run.
    except FileNotFoundError:
        print(f"Couldn't find the track: {name}")

# Deleted, because it's not needed after the above.
del track_names

###############################################################################
# Section 2: Defining classes.
###############################################################################


class Player(SPRITE):
    """Used, of course, to make the player."""

    def __init__(self):
        super().__init__()

        self.image = PLAYER_STATE_NORMAL_IMAGE
        self.rect = self.image.get_rect(centerx=HORIZONTAL_OFFSET, centery=VERTICAL_OFFSET)
    
        self.speed = PLAYER_SPEED_NORMAL
        
        # Represents how much further (the number of maze cells)
        # the player can move before their powerup runs out.
        # 0 means that the powerup has run out.
        self.powerup_distance = 0
        # Represents what powerup the player currently has.
        # 0 means that the player doesn't have a powerup (yet).
        self.powerup_type = 0
    
    def player_input(self) -> None:
        """Handle player input as well as maze wall collision detection."""

        keys_pressed = pygame.key.get_pressed()

        if any(keys_pressed):
            # If the player is pressing w,
            if keys_pressed[pygame.K_w]:
                # then move them up.
                self.rect.y -= self.speed

                # However, if they're now in a wall,
                if SPRITECOLLIDEANY(self, maze_walls):
                    # then move them back to where they were.
                    self.rect.y += self.speed
            # If they're not moving up,
            # then check for s being pressed.
            # If s has been pressed,
            elif keys_pressed[pygame.K_s]:
                # then move them down.
                self.rect.y += self.speed

                if SPRITECOLLIDEANY(self, maze_walls):
                    self.rect.y -= self.speed
            
            if keys_pressed[pygame.K_a]:
                self.rect.x -= self.speed

                if SPRITECOLLIDEANY(self, maze_walls):
                    self.rect.x += self.speed
            elif keys_pressed[pygame.K_d]:
                self.rect.x += self.speed

                if SPRITECOLLIDEANY(self, maze_walls):
                    self.rect.x -= self.speed

            if self.powerup_distance > 0:
                self.powerup_distance -= self.speed / AVERAGE_CELL_WIDTH

                # Once the power distance is 0,
                if self.powerup_distance <= 0:
                    # then reset the player to their normal state.
                    self.speed = PLAYER_SPEED_NORMAL
                    self.image = PLAYER_STATE_NORMAL_IMAGE

                    self.powerup_type = 0
    
    def enemy_collision(self) -> None:
        """Checks to see if the player is touching a enemy."""

        # Check to see if we have actually collided with a enemy first.
        collided_sprite = SPRITECOLLIDEANY(self, enemies)

        # If collided_sprite isn't None, then do stuff to the sprite.
        if collided_sprite:
            # Once a enemy has been touched, it should die.
            enemies.remove(collided_sprite)

            # If player speed hasn't gotten a powerup,
            if self.powerup_type == 0:
                # then send the player back to the start.
                self.rect.centerx, self.rect.centery = HORIZONTAL_OFFSET, VERTICAL_OFFSET
            else:
                # If the player got a powerup, then make their
                # speed and appearance normal again and let them go on.
                self.speed = PLAYER_SPEED_NORMAL
                self.image = PLAYER_STATE_NORMAL_IMAGE

                self.powerup_type = 0

    def powerup_collision(self) -> None:
        """Checks to see if the player is touching a power-up."""

        # Check to see if we have actually collided with a power-up first.
        collided_sprite = SPRITECOLLIDEANY(self, powerups)

        # If collided_sprite isn't None, then do stuff to the sprite.
        if collided_sprite:

            # Check and see what kind of power-up it is.
            match collided_sprite.type:
                # Power-up.
                case 1:
                    self.image = PLAYER_STATE_FAST_IMAGE
                    self.speed = PLAYER_SPEED_FAST

                    self.powerup_type = 1
                # Power-down.
                case 2:
                    self.image = PLAYER_STATE_SLOW_IMAGE
                    self.speed = PLAYER_SPEED_SLOW

                    self.powerup_type = 2
                # The end of the maze.
                # Will be used to go on to the next maze.
                case 3:
                    return "End"
            
            # Once a power-up has been "collected", the player shouldn't be able to get
            # it again.
            powerups.remove(collided_sprite)
            
            self.powerup_distance = (((COLUMNS*ROWS) ** 0.5) - 1) * 0.875
        

class PowerUp(SPRITE):
    """Used to create stuff that the player can collect."""

    def __init__(self, type: int, **kwargs):
        super().__init__()

        self.image = pygame.Surface((HORIZONTAL_OFFSET, VERTICAL_OFFSET))
        self.rect = self.image.get_rect(**kwargs)

        match type:
            # Power-up.
            case 1:
                self.image = POWERUP_FAST_IMAGE
            # Power-down.
            case 2:
                self.image = POWERUP_SLOW_IMAGE
            # The end of the maze.
            case 3:
                self.image = POWERUP_END_IMAGE

        self.type = type
    
    @staticmethod
    def powerup_generation() -> pygame.sprite.Group:
        """Generate sprites for the power-ups of a maze."""

        powerup_group = pygame.sprite.Group()

        # Places each row of powerups.
        for row in range(1, ROWS + 1):
            # Places each column of powerups.
            for column in range(1, COLUMNS + 1):
                if randint(1, powerup_chance) == 1:
                    # Calculates where the powerup should be placed.
                    WIDTH_times_row = -VERTICAL_OFFSET + VERTICAL_CELL_HEIGHT*row
                    WIDTH_times_column = -HORIZONTAL_OFFSET + HORIZONTAL_CELL_WIDTH*column

                    # Bad powerups are slightly more common.
                    # This makes the good powerups feel more special / valuable.
                    selected_powerup_type = choices([1, 2], [40, 60], k=1)[0]

                    powerup = PowerUp(
                        type=selected_powerup_type,
                        centerx=WIDTH_times_column,
                        centery=WIDTH_times_row
                    )
                
                    powerup_group.add(powerup)
        
        # These 2 lines are here so that even if no powerups generate,
        # the end still can generate properly.
        WIDTH_times_row = -VERTICAL_OFFSET + VERTICAL_CELL_HEIGHT*row
        WIDTH_times_column = -HORIZONTAL_OFFSET + HORIZONTAL_CELL_WIDTH*column
        
        # Add an end point for the maze, so the player can go on to the next maze / level.
        powerup_group.add(PowerUp(3, centerx=WIDTH_times_column, centery=WIDTH_times_row))

        return powerup_group


class Enemy(SPRITE):
    """Used to create enemies for the maze."""

    def __init__(self, enemy_type: int, enemy_powerup_type: int, direction: int, **kwargs):
        super().__init__()

        self.image = pygame.Surface((HORIZONTAL_OFFSET, VERTICAL_OFFSET))

        self.enemy_type = enemy_type
        self.enemy_powerup_type = enemy_powerup_type

        # Type 1 refers to normal enemies that bounce back and forth in certain directions.
        if enemy_type == 1:
            match enemy_powerup_type:
                # Powered-up / fast type 1 enemy.
                case 1:
                    self.image = ENEMY_STATE_TYPE_1_FAST_IMAGE
                    self.speed = ENEMY_SPEED_FAST
                # Powered-down / slow type 1 enemy.
                case 2:
                    self.image = ENEMY_STATE_TYPE_1_SLOW_IMAGE
                    self.speed = ENEMY_SPEED_SLOW
                # Normal type 1 enemy.
                case 3:
                    self.image = ENEMY_STATE_TYPE_1_NORMAL_IMAGE
                    self.speed = ENEMY_SPEED_NORMAL
        # Type 2 is for enemies that keep moving in random directions.
        elif enemy_type == 2:
            match enemy_powerup_type:
                # Powered-up / fast type 2 enemy.
                case 1:
                    self.image = ENEMY_STATE_TYPE_2_FAST_IMAGE
                    self.speed = ENEMY_SPEED_FAST
                # Powered-down / slow type 2 enemy.
                case 2:
                    self.image = ENEMY_STATE_TYPE_2_SLOW_IMAGE
                    self.speed = ENEMY_SPEED_SLOW
                # Normal type 2 enemy.
                case 3:
                    self.image = ENEMY_STATE_TYPE_2_NORMAL_IMAGE
                    self.speed = ENEMY_SPEED_NORMAL
        
        self.rect = self.image.get_rect(**kwargs)

        self.direction = direction
    
    @staticmethod
    def enemy_generation() -> pygame.sprite.Group:
        """Generate sprites for the enemies of a maze."""

        enemy_group = pygame.sprite.Group()

        # Places each row of enemies. 
        for row in range(1, ROWS + 1):
            # Places each column of enemies. 
            for column in range(1, COLUMNS + 1):
                if randint(1, enemy_chance) == 1:
                    # Calculates where the enemy should be placed.
                    WIDTH_times_row = -VERTICAL_OFFSET + VERTICAL_CELL_HEIGHT*row
                    WIDTH_times_column = -HORIZONTAL_OFFSET + HORIZONTAL_CELL_WIDTH*column

                    # Explanation: The chances of an enemy being type 1 is 75% and so on.
                    selected_enemy_type = choices([1, 2], [75, 25], k=1)[0]
                    # Explanation: The chances of an enemy having a powerup of type 1 is 25% and so on.
                    selected_enemy_powerup_type = choices([1, 2, 3], [25, 15, 60], k=1)[0]

                    enemy = Enemy(
                        enemy_type=selected_enemy_type,
                        enemy_powerup_type=selected_enemy_powerup_type,
                        direction=randint(1, 4),
                        centerx=WIDTH_times_column,
                        centery=WIDTH_times_row
                    )

                    enemy_group.add(enemy)

        return enemy_group
    
    def powerup_collision(self) -> None:
        """Checks to see if an enemy is touching a power-up."""

        # Pretty much the same as the powerup_collision function in the Player class.

        # Check to see if we have actually collided with a power-up first.
        collided_sprite = SPRITECOLLIDEANY(self, powerups)

        # If collided_sprite isn't None, then do stuff to the sprite.
        if collided_sprite:
            if self.enemy_type == 1:
                # Check and see what kind of power-up it is.
                match collided_sprite.type:
                    # Power-up.
                    case 1:
                        self.image = ENEMY_STATE_TYPE_1_FAST_IMAGE
                        self.speed = ENEMY_SPEED_FAST
                    # Power-down.
                    case 2:
                        self.image = ENEMY_STATE_TYPE_1_SLOW_IMAGE
                        self.speed = ENEMY_SPEED_SLOW
                    # An enemy shouldn't be able to collect the end of the maze powerup,
                    # so we end the function before it gets collected (removed).
                    case 3:
                        return None
            elif self.enemy_type == 2:
                # Check and see what kind of power-up it is.
                match collided_sprite.type:
                        # Powered-up / fast type 2 enemy.
                    case 1:
                        self.image = ENEMY_STATE_TYPE_2_FAST_IMAGE
                        self.speed = ENEMY_SPEED_FAST
                    # Powered-down / slow type 2 enemy.
                    case 2:
                        self.image = ENEMY_STATE_TYPE_2_SLOW_IMAGE
                        self.speed = ENEMY_SPEED_SLOW
                    # An enemy shouldn't be able to collect the end of the maze powerup,
                    # so we end the function before it gets collected (removed).
                    case 3:
                        return None
            
            # Once a power-up has been "collected", the enemy shouldn't be able to get
            # it again.
            powerups.remove(collided_sprite)
                     
    def update(self):
        """Mainly used to move each enemy and have it act.
        Also checks for maze wall collision detection.
        Also checks for powerup collision detection.
        """

        if self.enemy_type == 1:
            # Movement.
            match self.direction:
                # If it's facing right,
                case 1:
                    # then move it to the right.
                    self.rect.x += self.speed

                    # Collision detection.
                    # If it's touching a wall,
                    if SPRITECOLLIDEANY(self, maze_walls):
                        # then go in the other / opposite direction.
                        self.direction = 3
                        self.rect.x -= self.speed
                case 2:
                    # Moving down.
                    self.rect.y += self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = 4
                        self.rect.y -= self.speed
                case 3:
                    # Moving to the left.
                    self.rect.x -= self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = 1
                        self.rect.x += self.speed
                case 4:
                    # Moving up.
                    self.rect.y -= self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = 2
                        self.rect.y += self.speed
        elif self.enemy_type == 2:
            # Movement.
            match self.direction:
                # If it's facing right,
                case 1:
                    # then move it to the right.
                    self.rect.x += self.speed

                    # Collision detection.
                    # If it's touching a wall,
                    if SPRITECOLLIDEANY(self, maze_walls):
                        # then go in a random direction.
                        self.direction = randint(1, 4)
                        self.rect.x -= self.speed
                case 2:
                    # Moving down.
                    self.rect.y += self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = randint(1, 4)
                        self.rect.y -= self.speed
                case 3:
                    # Moving to the left.
                    self.rect.x -= self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = randint(1, 4)
                        self.rect.x += self.speed
                case 4:
                    # Moving up.
                    self.rect.y -= self.speed

                    if SPRITECOLLIDEANY(self, maze_walls):
                        self.direction = randint(1, 4)
                        self.rect.y += self.speed
        
        # Explains itself, but this checks for collisions with powerups.
        self.powerup_collision()


class MazeWall(SPRITE):
    """Used to create the individual walls of a maze."""

    def __init__(self, width: int, height: int, **kwargs):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill("#ffffff")
        self.rect = self.image.get_rect(**kwargs)
    
    @staticmethod
    def maze_generation() -> pygame.sprite.Group:
        """Generate sprites for the walls of a maze."""

        # I know that the maze generation is a bit questionable
        # and odd, but it works fine, Imo.

        maze_wall_group = pygame.sprite.Group()

        # Determines the range of directions that maze walls can face.
        direction_start = 1
        direction_end = 4

        # This changes the maze wall RNG sometimes, so that a greater variety
        # of mazes can generate.
        if randint(1, 4) == 1:
            direction_start = randint(1, 2)

            if direction_start == 1:
                direction_end = randint(3, 4)
            else:
                direction_end = 4

        # Places each row of maze walls.
        for row in range(1, ROWS):
            # Calculates where the player should be placed vertically (what row).
            WIDTH_times_row = VERTICAL_CELL_HEIGHT * row
            # Places each column of maze walls.
            for column in range(1, COLUMNS):
                # Calculates where the player should be placed horizontally (what column).
                WIDTH_times_column = HORIZONTAL_CELL_WIDTH * column

                direction = randint(direction_start, direction_end)

                # Attempts to make maze walls somewhat more connected.
                if randint(1, 8) == 1:
                    match direction:
                        case 2:
                            direction = randint(1, 3)
                        case 1 | 3 | 4:
                            direction = 4

                match direction:
                    case 1:
                        # Create a wall facing up.
                        maze_wall = MazeWall(
                            width=1,
                            height=VERTICAL_CELL_HEIGHT,
                            x=WIDTH_times_column,
                            bottom=WIDTH_times_row
                        )
                    case 2:
                        # Create a wall facing right.
                        maze_wall = MazeWall(
                            width=HORIZONTAL_CELL_WIDTH,
                            height=1,
                            x=WIDTH_times_column,
                            y=WIDTH_times_row
                        )
                    case 3:
                        # Create a wall facing down.
                        maze_wall = MazeWall(
                            width=1,
                            height=VERTICAL_CELL_HEIGHT,
                            x=WIDTH_times_column,
                            y=WIDTH_times_row
                        )
                    case 4:
                        # Create a wall facing left.
                        maze_wall = MazeWall(
                            width=HORIZONTAL_CELL_WIDTH,
                            height=1,
                            y=WIDTH_times_row,
                            right=WIDTH_times_column
                        )

                maze_wall_group.add(maze_wall)

        # Add a boundary to the maze, so that the player can't escape it.
        maze_wall_group.add(
            MazeWall(SCREEN_WIDTH, 1, x=0, y=0),  # Top wall.
            MazeWall(1, SCREEN_HEIGHT, x=MAZE_WIDTH - 1, y=0),  # Right wall. Shifted 1 (pixel) to the left, so you can see it.
            MazeWall(SCREEN_WIDTH, 1, x=0, y=MAZE_HEIGHT - 1),  # Bottom wall. Shifted 1 to up, so you can see it.
            MazeWall(1, SCREEN_HEIGHT, x=0, y=0)  # Left wall.
        )

        return maze_wall_group


###############################################################################
# Section 3: Defining functions.
###############################################################################


def draw_stuff() -> None:
    """Used to draw things (creates a frame)."""

    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))
    player.draw(SCREEN)
    maze_walls.draw(SCREEN)
    powerups.draw(SCREEN)
    enemies.draw(SCREEN)


###############################################################################
# Section 4: The gameplay loop (and other stuff).
###############################################################################

# The game loop.
while True:
    # Sets up the chances of stuff appearing in the maze.
    powerup_chance = abs(round((COLUMNS*ROWS - 15)/(COLUMNS*ROWS / 61.5234375) * uniform(uniform(0, 1.1289), 1.1289)))
    enemy_chance = abs(round((COLUMNS*ROWS - 15)/(COLUMNS*ROWS / 123.046875) * uniform(uniform(0, 1.1289), 1.1289)))

    # Every now and then, there will either be a really good maze (lots of powerups)
    # or a really challenging maze (lots of enemies).
    if randint(1, 50) == 1:
        if randint(1, 3) == 1:
            powerup_chance = randint(3, 4)
        else:
            enemy_chance = randint(4, 5)

            # Stop any music currently playing
            pygame.mixer.stop()
            # and try to play the epic music (not included).
            try:
                MUSIC[0].play()
            except IndexError:
                print("Couldn't find the track: MUSIC[0].")

    # All of these are groups.
    player = pygame.sprite.GroupSingle(Player())
    maze_walls = MazeWall.maze_generation()
    powerups = PowerUp.powerup_generation()
    enemies = Enemy.enemy_generation()

    # Repeats for as long as you are in a maze.
    while True:
        # The event loop. Only used to end the game.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        draw_stuff()

        player.sprite.player_input()

        # If it returns "End" rather than None,
        if player.sprite.powerup_collision() == "End":
            # then go on to the next maze.
            break

        # Move / update all of the enemies.
        # This function runs on every enemy in the maze.
        enemies.update()

        player.sprite.enemy_collision()

        # Chooses the music.
        # If there is no music, then skip this all together.
        # Also, if no music is playing, then randomly choose some music and play it.
        # Also, if music is playing, then the following will be ignored.
        if MUSIC and pygame.mixer.get_busy() == False:
            selected_music = MUSIC[randint(1, len(MUSIC) - 1)]
            # The music will fade in for 7.5 seconds.
            selected_music.play(fade_ms=7500)
            # The end of the music will start to fade out with 5 seconds remaining.
            # Currently disabled, because it doesn't work.
            # selected_music.fadeout(int(selected_music.get_length() * 1000 - 5000))

        # Extra stuff.
        pygame.display.update()
        CLOCK.tick(60)