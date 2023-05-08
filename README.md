# gifsplitter
This is a script to break down GIFs into frames, intended to help when compiling Flipper Zero Animations.

# Usage
```console
python gifsplitter.py wips
```
wips would be a folder with the gifs in it. You can pass in relative or absolute paths. The script will go through each GIF in the folder, create a subfolder in it with the same name, and save the frames as frame_x.png

## Dependencies
- imageio
- pillow

This is based on mnenkov's [gif2zip](https://github.com/mnenkov/flipper-zero-animations/blob/main/gif2zip/gif2zip.txt) script
