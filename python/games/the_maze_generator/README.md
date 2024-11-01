# The Maze Generator

This is a game where you (a red square) must traverse a maze to the end (a green square).

Along the way, there are powerups and enemies. Some may help you and some may not.

In order to move, you use WASD.

In-game images can be modified by changing the images in the sprites folder.

## Powerups

1. The yellow powerup.

    This one makes you temporarily faster.

2. The cyan powerup.

    This one makes you temporarily slower. It's more like an obstacle.

    Also, they're inspired by the poison mushrooms from Super Mario Bros.: The Lost Levels.

## Enemies

Enemies will pick a random direction upon spawning and move in it.

When an enemy is touched by the player, they will die. However, if
the player didn't have a powerup when they touched the enemy, then
they will die as well. If the player did have a powerup, then they
simply lose it.

Also, enemies can collect powerups as well and they can even spawn
with a powerup equipped.

There are 2 types of enemies.

1. Type 1.

    These enemies are (usually) dark blue and, when they touch a wall, they will move in the opposite direction.

2. Type 2.

    These enemies are (usually) purple / violet and, when they touch a wall, they will then move in a random direction.
