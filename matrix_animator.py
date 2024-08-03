import threading
import pygame
import time

class StateManager:
    def __init__(self):
        self.state = {}

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

class MatrixAnimator(threading.Thread):
    def __init__(self, state_manager):
        super().__init__()
        self.state_manager = state_manager
        self.running = True
        self.screen = pygame.display.set_mode((700, 700))

    def run(self):
        while self.running:
            frames = self.state_manager.get('frames')
            if not frames:
                continue

            current_frame_index = self.state_manager.get('current_frame_index')
            frame, delay = frames[current_frame_index]

            self.draw_frame(frame)
            time.sleep(delay)
            current_frame_index = (current_frame_index + 1) % len(frames)
            self.state_manager.set('current_frame_index', current_frame_index)

    def stop(self):
        self.running = False

    def draw_frame(self, frame):
        self.screen.fill((0, 0, 0))
        cell_size = 100
        for y, row in enumerate(frame):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
        pygame.display.flip()
