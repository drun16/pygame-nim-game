import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
background_image = pygame.image.load("Nimaiball.png")
clock = pygame.time.Clock()
running = True
ai_delay_start_time = None  # Variable to track the AI's delay start time
AI_DELAY_MS = 1000  # Delay in milliseconds (e.g., 1 second)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Ball settings
BALL_RADIUS = 20
BALL_SPACING = 50
ROW_1_Y = 250
ROW_2_Y = 350

# Button settings
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50
BUTTON_SPACING = 10
BUTTON_START_Y = 450
BUTTON_START_X = 50

# Game state
row_1 = [1] * 9  # 9 balls in row 1
row_2 = [1] * 9  # 9 balls in row 2
player_turn = True  # True if it's the human player's turn
game_over = False
winner = None

# Font
font = pygame.font.Font(None, 36)

# Buttons for player actions
actions = [
    (0, 1), (0, 2), (0, 3),  # Take balls from row 1
    (1, 2), (2, 1), (1,1),# Take balls from row 2
    (1, 0), (2, 0), (3, 0)   # Mixed row selections
]
buttons = []

def create_buttons():
    """Create buttons for each action."""
    for i, action in enumerate(actions):
        x = BUTTON_START_X + (BUTTON_WIDTH + BUTTON_SPACING) * (i % 3)
        y = BUTTON_START_Y + (BUTTON_HEIGHT + BUTTON_SPACING) * (i // 3)
        buttons.append((pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT), action))

def draw_buttons():
    """Draw buttons for player actions."""
    for rect, action in buttons:
        # Disable invalid buttons
        if not is_action_valid(action):
            pygame.draw.rect(screen, DARK_GRAY, rect)
        else:
            pygame.draw.rect(screen, GRAY, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        text = font.render(f"{action}", True, BLACK)
        screen.blit(text, (rect.x + rect.width // 2 - text.get_width() // 2,
                           rect.y + rect.height // 2 - text.get_height() // 2))

def draw_balls():
    """Draw the rows of balls."""
    for i, ball in enumerate(row_1):
        color = RED if ball else WHITE
        pygame.draw.circle(screen, color, (100 + i * BALL_SPACING, ROW_1_Y), BALL_RADIUS)
        pygame.draw.circle(screen, WHITE, (100 + i * BALL_SPACING, ROW_1_Y), BALL_RADIUS, 1)

    for i, ball in enumerate(row_2):
        color = BLUE if ball else WHITE
        pygame.draw.circle(screen, color, (100 + i * BALL_SPACING, ROW_2_Y), BALL_RADIUS)
        pygame.draw.circle(screen, WHITE, (100 + i * BALL_SPACING, ROW_2_Y), BALL_RADIUS, 1)

def check_game_over():
    """Check if the game is over."""
    if sum(row_1) + sum(row_2) == 0:
        return True
    return False

# def is_first_move():
#     """Check if it's the first move of the game."""
#     return first_move

def is_action_valid(action):
    """Check if the action is valid based on the remaining balls."""
    row_1_count, row_2_count = action
    return sum(row_1) >= row_1_count and sum(row_2) >= row_2_count

def handle_player_action(action):
    """Process the player's selected action."""
    global row_1, row_2
    row_1_count, row_2_count = action
    balls_picked = 0

    # Take balls from row 1
    for i in range(len(row_1)):
        if balls_picked >= row_1_count:
            break
        if row_1[i] == 1:
            row_1[i] = 0
            balls_picked += 1

    # Take balls from row 2
    balls_picked = 0
    for i in range(len(row_2)):
        if balls_picked >= row_2_count:
            break
        if row_2[i] == 1:
            row_2[i] = 0
            balls_picked += 1

def calculate_nim_sum():
    """Calculate the Nim sum of the rows."""
    return sum(row_1) ^ sum(row_2)

def ai_turn():
    """AI logic to pick balls based on Nim-sum strategy."""
    global row_1, row_2
    nim_sum = calculate_nim_sum()

    def make_move(row_index, balls_to_remove):
        """Helper to make the AI move on a specific row."""
        row = row_1 if row_index == 0 else row_2
        balls_removed = 0
        for i in range(len(row)):
            if balls_removed >= balls_to_remove:
                break
            if row[i] == 1:
                row[i] = 0
                balls_removed += 1

    if nim_sum != 0:
        # Try to force a win by making the Nim sum zero
        for row_index, row in enumerate([row_1, row_2]):
            for i in range(len(row)):
                if row[i] == 1 and (sum(row) ^ nim_sum) < sum(row):
                    row[i] = 0
                    make_move(row_index, 1)
                    return
    else:
        # If the Nim-sum is zero, select a random valid move
        while True:
            balls_to_pick = random.randint(1, min(3, sum(row_1) + sum(row_2)))
            if balls_to_pick != 1 or (sum(row_1) != 1 and sum(row_2) != 1):
                break
        make_move(0, balls_to_pick)

def ai_move_for_equal_balls():
    """AI fallback logic when the rows have an equal number of balls."""
    global row_1, row_2

    # Choose a valid action that removes a minimal number of balls
    for row_index, row in enumerate([row_1, row_2]):
        for count in range(1, min(3, sum(row)) + 1):
            if is_action_valid((count, 0) if row_index == 0 else (0, count)):
                move = (count, 0) if row_index == 0 else (0, count)
                handle_player_action(move)
                return

# Create the buttons
create_buttons()

# Main loop
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and player_turn and not game_over:
            # Check if a button was clicked
            for rect, action in buttons:
                if rect.collidepoint(event.pos) and is_action_valid(action):
                    handle_player_action(action)
                    player_turn = False
                    ai_delay_start_time = pygame.time.get_ticks()  # Record time when AI's delay starts

    # AI's turn
    if not player_turn and not game_over:
        current_time = pygame.time.get_ticks()
        if ai_delay_start_time is not None and current_time - ai_delay_start_time >= AI_DELAY_MS:
            ai_turn()
            player_turn = True
            ai_delay_start_time = None  # Reset the timer after the AI moves

    # Check if the game is over
    if check_game_over():
        game_over = True
        winner = "Human" if player_turn else "AI"

    # Render game
    screen.blit(background_image, (0, 0))  # Draw background
    draw_balls()
    draw_buttons()

    # Display turn or winner
    if game_over:
        text = font.render(f"Game Over! Winner: {'Human' if winner == 'Human' else 'AI'}", True, GREEN)
    else:
        text = font.render("Your Turn!" if player_turn else "AI's Turn!", True, WHITE)
    screen.blit(text, (640 - text.get_width() // 2, 50))

    # Flip the display
    pygame.display.flip()
    clock.tick(60)  # Limit FPS to 60
