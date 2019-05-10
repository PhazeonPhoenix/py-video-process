# py-video-process

Install latest python 3 and `pip`

Run following:

```
pip install moviepy
```

## What Does It Do?

This script can take up to 3 video files, combine the clips sequentially and position a
logo in the lower right corner of the screen for the primary input video. It
also applies a short fade in and out on all the video clips.

## Simple usage

This is designed to be simple to use at the outset but still has room to
customize if desired. If you organize your recordings similar to me, you have
a directory for each series and the videos sit there with a sequential name.
This script can be used very simply with such an arrangement.

* Place a copy of `process.py` in the directory with your videos.
* Copy your logo into the directory and name it `logo.png`
* Copy intro (at the beginning) and outro (at the end) videos into the directory
  and name them `intro.mp4` and `outro.mp4`.
* With a File Explorer window, drag and drop a video file onto `process.py`.
* Dropped file is processed, and outputted in the same directory with `output`
  appended to the name.

## Advanced Usage

Quite a few command line options to exploit to tweak the output.

```
>python process.py -h
usage: process.py [-h] [--intro INTRO] [--outro OUTRO] [--logo LOGO]
                  [--logo-size LOGO_SIZE]
                  [--logo-margin-bottom LOGO_MARGIN_BOTTOM]
                  [--logo-margin-right LOGO_MARGIN_RIGHT]
                  [--fadein-duration FADEIN_DURATION]
                  [--fadeout-duration FADEOUT_DURATION]
                  [--intro-fadein-duration INTRO_FADEIN_DURATION]
                  [--intro-fadeout-duration INTRO_FADEOUT_DURATION]
                  [--outro-fadein-duration OUTRO_FADEIN_DURATION]
                  [--outro-fadeout-duration OUTRO_FADEOUT_DURATION] [-o OUT]
                  [--overwrite] [--bitrate BITRATE]
                  [--audio_bitrate AUDIO_BITRATE] [-d]
                  input

Process a video file, optionally adding a logo, an intro and an outro.

positional arguments:
  input                 The primary input video file to process.

optional arguments:
  -h, --help            show this help message and exit
  --intro INTRO         The intro video file to use. By default, 'intro.mp4'
                        is used. You can disable with a value of 'none'.
  --outro OUTRO         The outro file to use. By default, 'outro.mp4' is
                        used. You can disable with a value of 'none'.
  --logo LOGO           The logo file to use. By default, 'logo.png' is used.
                        You can disable with a value of 'none'.
  --logo-size LOGO_SIZE
                        The maximum size of the logo after resizing. The
                        logo's aspect ratio is maintained.
  --logo-margin-bottom LOGO_MARGIN_BOTTOM
                        The amount of pixels to place between the bottom of
                        the logo and the bottom of the input video.
  --logo-margin-right LOGO_MARGIN_RIGHT
                        The amount of pixels to place between the right of the
                        logo and the right of the input video.
  --fadein-duration FADEIN_DURATION
                        Duration in seconds of the fadein effect applied to
                        the input video. A value of 0 would disable it.
  --fadeout-duration FADEOUT_DURATION
                        Duration in seconds of the fadeout effect applied to
                        the input video. A value of 0 would disable it.
  --intro-fadein-duration INTRO_FADEIN_DURATION
                        Duration in seconds of the fadein effect applied to
                        the intro video. A value of 0 would disable it.
  --intro-fadeout-duration INTRO_FADEOUT_DURATION
                        Duration in seconds of the fadeout effect applied to
                        the intro video. A value of 0 would disable it.
  --outro-fadein-duration OUTRO_FADEIN_DURATION
                        Duration in seconds of the fadein effect applied to
                        the outro video. A value of 0 would disable it.
  --outro-fadeout-duration OUTRO_FADEOUT_DURATION
                        Duration in seconds of the fadeout effect applied to
                        the outro video. A value of 0 would disable it.
  -o OUT, --out OUT     The output filename. By default, this is the input
                        file plus '.output'. Example 'input.output.mp4'
  --overwrite           Overwrite output file if it exists.
  --bitrate BITRATE     Output video bitrate.
  --audio_bitrate AUDIO_BITRATE
                        Output audio bitrate.
  -d, --debug           Output debugging information.
```
