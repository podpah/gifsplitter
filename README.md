# gifsplitter
This is a script to break down GIFs into frames, intended to help when compiling Flipper Zero Animations.

# Usage
```console
python gifsplitter.py wips
```
wips would be a folder with the gifs in it. You can pass in relative or absolute paths. The script will go through each GIF in the folder, create a subfolder in it with the same name, and save the frames as frame_x.png

It also creates a basic meta.txt for you:
```
Filetype: Flipper Animation
Version: 1

Width: 128
Height: 64
Passive frames: 10 # The passive frames changes in line with how many frames your GIF has
Active frames: 0
Frames order: 0 1 2 3 4 5 6 7 8 9 # And same goes for the frame order, it'll go from 0 to the number of frames -1
Active cycles: 0
Frame rate: 7
Duration: 3600
Active cooldown: 0

Bubble slots: 0

```

## Dependencies
- imageio
- pillow

This is based on mnenkov's [gif2zip](https://github.com/mnenkov/flipper-zero-animations/blob/main/gif2zip/gif2zip.txt) script
