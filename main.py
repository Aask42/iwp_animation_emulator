import pygame
import time
import random
from matrix_animator import MatrixAnimator, StateManager
from test_animations import animations, generate_eq_frames, generate_sine_wave

def draw_menu(screen, options, selected_index):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 36)
    for i, option in enumerate(options):
        color = (255, 255, 255) if i == selected_index else (100, 100, 100)
        text = font.render(option, True, color)
        screen.blit(text, (50, 50 + i * 40))
    pygame.display.flip()

def main():
    # Create StateManager instance
    state_manager = StateManager()

    # Pygame setup for menu
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Select Animation")
    clock = pygame.time.Clock()
    
    # Menu options
    options = list(animations.keys()) + ["Exit"]
    selected_index = 0

    running = True
    in_menu = True
    animator = None

    while running:
        if in_menu:
            draw_menu(screen, options, selected_index)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_index = (selected_index - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected_index = (selected_index + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        selected_option = options[selected_index]
                        if selected_option == "Exit":
                            running = False
                        else:
                            frames = animations[selected_option] if selected_option in animations else generate_eq_frames(10)
                            for frame in frames:
                                print(f"{frames}")
                            state_manager.set('frames', frames)
                            state_manager.set('current_frame_index', 0)
                            
                            # Create and start MatrixAnimator
                            animator = MatrixAnimator(state_manager)
                            animator.start()
                            in_menu = False
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    animator.stop()
                    animator.join()
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        animator.stop()
                        animator.join()
                        in_menu = True

        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    main()
