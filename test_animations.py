# test_animations.py
import random
# Jump Man frames (as provided)
jump_man_frames = [
    (
        [[0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]],
        1.0)
    ,
    
        ([[0, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]],
        0.25)
    ,
    
        ([[0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]],
        1.0)
    ,
    
        ([[0, 0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1]],
        2)
    ,
]


import math
def generate_sine_wave(frames, frequency=1, amplitude=3):
    wave = []

    for frame in range(frames):
        matrix = []
        for y in range(7):
            row = [0] * (7 if y < 2 else 6)  # First two rows have 7 columns, rest have 6 columns
            x = int(amplitude * math.sin(2 * math.pi * frequency * (frame + y) / frames) + amplitude)
            if y < 2:
                row[x % 7] = 1
            else:
                row[x % 6] = 1
            matrix.append(row)
        wave.append((matrix, 0.1))  # Use a duration of 0.1 seconds for each frame

    return wave
#waves = generate_sine_wave()
#print(waves)
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
    "Fake EQ": fake_frames,  # Reference to the function, 
    "Gen SIN wave": generate_sine_wave(10)
}

#b = generate_eq_frames(4)
#print(b)