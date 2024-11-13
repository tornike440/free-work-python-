import random
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)
sh, sw = stdscr.getmaxyx()  # Get screen size
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)  # Timeout in milliseconds (controls the game speed)

# Shapes of Tetriminos
TETROMINOS = [
    [[1, 1, 1], [0, 1, 0]],  # T-shape
    [[1, 1, 0], [0, 1, 1]],  # Z-shape
    [[0, 1, 1], [1, 1, 0]],  # S-shape
    [[1, 1, 1, 1]],           # I-shape
    [[1, 1], [1, 1]],         # O-shape
    [[1, 1, 1], [1, 0, 0]],  # L-shape
    [[1, 1, 1], [0, 0, 1]],  # J-shape
]

# Colors for Tetriminos
COLORS = [curses.COLOR_CYAN, curses.COLOR_YELLOW, curses.COLOR_MAGENTA, 
          curses.COLOR_GREEN, curses.COLOR_BLUE, curses.COLOR_RED, curses.COLOR_WHITE]

# Function to initialize a new tetrimino
def new_tetrimino():
    shape = random.choice(TETROMINOS)
    color = random.choice(COLORS)
    return shape, color

# Function to check if the move is valid
def valid_move(tetrimino, offset, grid):
    shape, color = tetrimino
    x, y = offset

    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                new_x = x + j
                new_y = y + i
                if new_x < 0 or new_x >= sw // 2 or new_y >= sh - 1 or grid[new_y][new_x] != 0:
                    return False
    return True

# Function to add the tetrimino to the grid
def add_to_grid(tetrimino, offset, grid):
    shape, color = tetrimino
    x, y = offset

    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                grid[y + i][x + j] = color

# Function to clear full lines
def clear_lines(grid):
    full_lines = [i for i, row in enumerate(grid) if all(cell != 0 for cell in row)]
    for i in full_lines:
        del grid[i]
        grid.insert(0, [0] * (sw // 2))
    return len(full_lines)

# Main game function
def main(stdscr):
    # Set up color pairs
    curses.start_color()
    for i in range(len(COLORS)):
        curses.init_pair(i + 1, COLORS[i], curses.COLOR_BLACK)

    # Game grid (rows x cols)
    grid = [[0] * (sw // 2) for _ in range(sh - 1)]

    score = 0
    offset = [sw // 4, 0]
    tetrimino = new_tetrimino()

    while True:
        # Handle user input
        key = w.getch()

        if key == ord('q'):  # Quit game if 'q' is pressed
            break
        if key == curses.KEY_LEFT:  # Move left
            if valid_move(tetrimino, (offset[0] - 1, offset[1]), grid):
                offset[0] -= 1
        if key == curses.KEY_RIGHT:  # Move right
            if valid_move(tetrimino, (offset[0] + 1, offset[1]), grid):
                offset[0] += 1
        if key == curses.KEY_DOWN:  # Move down faster
            if valid_move(tetrimino, (offset[0], offset[1] + 1), grid):
                offset[1] += 1
        if key == curses.KEY_UP:  # Rotate tetrimino
            rotated_tetrimino = [list(row) for row in zip(*tetrimino[0][::-1])]  # 90-degree rotation
            if valid_move((rotated_tetrimino, tetrimino[1]), offset, grid):
                tetrimino = (rotated_tetrimino, tetrimino[1])

        # Move the tetrimino down
        if not valid_move(tetrimino, (offset[0], offset[1] + 1), grid):
            add_to_grid(tetrimino, offset, grid)
            score += clear_lines(grid)
            tetrimino = new_tetrimino()  # Get a new tetrimino
            offset = [sw // 4, 0]  # Reset position

            # Game over if the new tetrimino doesn't fit
            if not valid_move(tetrimino, offset, grid):
                break
        else:
            offset[1] += 1

        # Render the game
        w.clear()
        for y in range(sh - 1):
            for x in range(sw // 2):
                color = grid[y][x]
                if color:
                    w.addstr(y, x * 2, "  ", curses.color_pair(color))

        # Draw the active tetrimino
        shape, color = tetrimino
        for i, row in enumerate(shape):
            for j, cell in enumerate(row):
                if cell:
                    w.addstr(offset[1] + i, (offset[0] + j) * 2, "  ", curses.color_pair(color))

        # Display the score
        w.addstr(0, 2, f"Score: {score}")

        # Refresh the screen
        w.refresh()

    # End game message
    w.clear()
    w.addstr(sh // 2, sw // 4, "Game Over!", curses.A_BOLD)
    w.refresh()
    w.getch()


if __name__ == "__main__":
    curses.wrapper(main)
