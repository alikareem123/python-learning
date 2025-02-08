import os
import time
import random
import msvcrt
from msvcrt import getch, kbhit

# Terminal clear function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Draw the game board
def draw_board(snake, food, score, width=20, height=10):
    for y in range(height):
        for x in range(width):
            if [y, x] == food:
                print("O", end="")  # Food
            elif [y, x] in snake:
                print("X", end="")  # Snake
            else:
                print(" ", end="")  # Empty space
        print("|")  # Right border
    print("=" * width)
    print(f"Score: {score}")

# Main game loop
def snake_game():
    width, height = 20, 10
    snake = [[5, 5]]  # Initial snake position
    direction = [0, 1]  # Initial movement (right)
    food = [random.randint(0, height - 1), random.randint(0, width - 1)]
    score = 0

    while True:
        clear_screen()
        draw_board(snake, food, score, width, height)

        # Wait for user input or continue moving
        if kbhit():
            key = getch()
            if key == b'\xe0':  # Special keys (arrows, etc.)
                key = getch()  # Read the next byte
                if key == b'H': direction = [-1, 0]  # Up arrow
                if key == b'P': direction = [1, 0]   # Down arrow
                if key == b'K': direction = [0, -1]  # Left arrow
                if key == b'M': direction = [0, 1]   # Right arrow
            elif key in [b'w', b'W']: direction = [-1, 0]  # W for up
            elif key in [b's', b'S']: direction = [1, 0]   # S for down
            elif key in [b'a', b'A']: direction = [0, -1]  # A for left
            elif key in [b'd', b'D']: direction = [0, 1]   # D for right

        # Move the snake
        new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

        # Check for collisions
        if (
            new_head in snake or  # Collision with itself
            new_head[0] < 0 or new_head[0] >= height or  # Top/Bottom wall
            new_head[1] < 0 or new_head[1] >= width  # Left/Right wall
        ):
            print("Game Over!")
            print(f"Final Score: {score}")
            break

        # Check if food is eaten
        if new_head == food:
            score += 1
            food = [random.randint(0, height - 1), random.randint(0, width - 1)]
        else:
            snake.pop()  # Remove tail

        snake.insert(0, new_head)  # Add new head
        time.sleep(0.4)  # Control game speed

if __name__ == "__main__":
    snake_game()