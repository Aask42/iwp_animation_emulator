# test_animations.py
import random
# Jump Man frames (as provided)
jump_man_frames = [
    [
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        1.0
    ],
    [
        [0, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        0.25
    ],
    [
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
        1.0
    ],
    [
        [0, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        2
    ],
]
def generate_eq_frames(num_frames):
    # Set up our frames object to generate groups of frames
    rows = 7
    columns = 6
    frames = []
    
    for frame_number in range(num_frames):
        # Create a new frame for each iteration
        new_frame = [[0] * columns for _ in range(rows)]
        
        # Randomly initialize equalizer levels for demonstration purposes
        levels = [random.randint(0, rows) for _ in range(columns)]
        peak_levels = [min(level + random.randint(0, 1), rows) for level in levels]

        for x in range(columns):
            for y in range(rows):
                if y < levels[x]:
                    new_frame[y][x] = 1
                else:
                    new_frame[y][x] = 0
        
        # Draw peak level
        for x in range(columns):
            peak_level_int = peak_levels[x]
            if peak_level_int > 0:
                new_frame[rows - peak_level_int][x] = 1
        
        frames.append([new_frame, 0.1])

    return frames

fake_frames = generate_eq_frames(10)

animations = {
    "Jump Man": jump_man_frames,
    "Fake EQ": fake_frames  # Reference to the function
}

#b = generate_eq_frames(4)
#print(b)