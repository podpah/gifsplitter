from PIL import Image
import os
import sys

# Get the folder path where the gifs are located
folder_path = rf"{sys.argv[1]}" # To be CLI callable

# Get list of gifs in the folder
gif_files = [f for f in os.listdir(folder_path) if f.endswith('.gif')]

# Iterate through all gifs
for gif_file in gif_files:
    gif_path = os.path.join(folder_path, gif_file)
    gif = Image.open(gif_path)
    # Get gif frames
    frames = []
    for i in range(0, gif.n_frames):
        gif.seek(i)
        frames.append(gif.copy())

    # Check if the number of frames is over 46
        if len(frames) > 46:
            i = len(frames)-1
            while len(frames) != 46:
                if i < 0:
                    break
                frames.pop(i)
                i -= 2
    # Create individual output folder for each gif
    gif_name = os.path.splitext(gif_file)[0]
    gif_output_folder = os.path.join(folder_path, gif_name)
    if not os.path.exists(gif_output_folder):
        os.makedirs(gif_output_folder)
    # Save frames to output folder
    for i in range(len(frames)):
        frames[i].save(os.path.join(gif_output_folder, f'frame_{i}.png'))
    print(f'{gif_name} completed')
    
# Confirmation message
print("Process completed!")
