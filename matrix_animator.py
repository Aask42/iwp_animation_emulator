import pygame
import time
import threading

class MatrixAnimator(threading.Thread):
    def __init__(self, state_manager, fps=60, cell_size=100, columns=7, rows=6, max_brightness=255):
        super().__init__()
        self.state_manager = state_manager
        self.fps = fps
        self.cell_size = cell_size
        self.columns = columns
        self.rows = rows
        self.max_brightness = max_brightness
        self.running = False

        # Initialize Pygame display
        pygame.init()
        self.screen = pygame.display.set_mode((columns * cell_size, rows * cell_size + 2 * cell_size))  # Extra space for LEDs
        pygame.display.set_caption("Matrix Animator")

    def run(self):
        clock = pygame.time.Clock()
        self.running = True
        while self.running:
            self.animate()
            clock.tick(self.fps)
        pygame.quit()

    def stop(self):
        self.running = False

    def apply_brightness(self, color, brightness):
        return tuple(brightness * c // 255 for c in color)

    def draw_frame(self, pattern):
        self.screen.fill((0, 0, 0))
        for y in range(min(self.rows, len(pattern))):  # Ensure we don't go out of bounds
            for x in range(min(self.columns, len(pattern[y]))):  # Ensure we don't go out of bounds
                if pattern[y][x] == 1:
                    color = self.apply_brightness((255, 255, 255), self.max_brightness)  # White for active level
                else:
                    color = (0, 0, 0)  # Off
                pygame.draw.rect(self.screen, color, pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        # Draw green and red LEDs in the extra column at the bottom (positions (0, 6) and (1, 6))
        if len(pattern) > 0 and len(pattern[0]) > 6 and pattern[0][6] == 1:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(6 * self.cell_size, 0, self.cell_size, self.cell_size))  # Green LED
        if len(pattern) > 1 and len(pattern[1]) > 6 and pattern[1][6] == 1:
            pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(6 * self.cell_size, self.cell_size, self.cell_size, self.cell_size))  # Red LED

        pygame.display.flip()

    def animate(self):
        frames = self.state_manager.get('frames', [])
        if not frames:
            return

        current_frame_index = self.state_manager.get('current_frame_index', 0)
        frame_data = frames[current_frame_index]
        pattern = frame_data[:-1]
        frame_time = frame_data[-1]
        hold_start_time = self.state_manager.get('hold_start_time', None)

        if hold_start_time is None:
            hold_start_time = time.time()
            self.state_manager.set('hold_start_time', hold_start_time)

        self.draw_frame(pattern)

        if time.time() - hold_start_time >= frame_time:
            current_frame_index = (current_frame_index + 1) % len(frames)
            self.state_manager.set('current_frame_index', current_frame_index)
            self.state_manager.set('hold_start_time', None)

class StateManager:
    def __init__(self):
        self.state = {}
        self.lock = threading.Lock()

    def get(self, key, default=None):
        with self.lock:
            return self.state.get(key, default)

    def set(self, key, value):
        with self.lock:
            self.state[key] = value
