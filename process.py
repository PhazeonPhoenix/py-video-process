import sys
import math
from argparse import ArgumentParser
from moviepy.editor import *
from moviepy.config import get_setting, change_settings
#change_settings({"FFMPEG_BINARY": r"F:\Python\ffmpeg.exe"})

parser = ArgumentParser(description="""
Process a video file, optionally adding a logo, an intro and an outro.
    """)
parser.add_argument("input", help="The primary input video file to process.")
parser.add_argument("--intro",
    default="intro.mp4",
    help="The intro video file to use. By default, 'intro.mp4' is used. You can disable with a value of 'none'."
    )
parser.add_argument("--outro",
    default="outro.mp4",
    help="The outro file to use. By default, 'outro.mp4' is used. You can disable with a value of 'none'."
    )
parser.add_argument("--logo",
    default="logo.png",
    help="The logo file to use. By default, 'logo.png' is used. You can disable with a value of 'none'."
    )
parser.add_argument("--logo-size",
    default=128,
    type=int,
    help="The maximum size of the logo after resizing. The logo's aspect ratio is maintained."
    )
parser.add_argument("--logo-margin-bottom",
    default=30,
    type=int,
    help="The amount of pixels to place between the bottom of the logo and the bottom of the input video."
    )
parser.add_argument("--logo-margin-right",
    default=30,
    type=int,
    help="The amount of pixels to place between the right of the logo and the right of the input video."
    )
parser.add_argument("--fadein-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadein effect applied to the input video. A value of 0 would disable it."
    )
parser.add_argument("--fadeout-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadeout effect applied to the input video. A value of 0 would disable it."
    )
parser.add_argument("--intro-fadein-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadein effect applied to the intro video. A value of 0 would disable it."
    )
parser.add_argument("--intro-fadeout-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadeout effect applied to the intro video. A value of 0 would disable it."
    )
parser.add_argument("--outro-fadein-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadein effect applied to the outro video. A value of 0 would disable it."
    )
parser.add_argument("--outro-fadeout-duration",
    default=.5,
    type=float,
    help="Duration in seconds of the fadeout effect applied to the outro video. A value of 0 would disable it."
    )
parser.add_argument("-o", "--out",
    help="The output filename. By default, this is the input file plus '.output'. Example 'input.output.mp4'"
    )
parser.add_argument("--overwrite",
    default=False,
    action="store_true",
    help="Overwrite output file if it exists."
    )
parser.add_argument("--bitrate",
    default=12000000, # for 60fps
    # default=8000000, # for 30fps
    type=int,
    help="Output video bitrate."
    )
parser.add_argument("--audio_bitrate",
    default=384000,
    type=int,
    help="Output audio bitrate."
    )
parser.add_argument("-d", "--debug",
    action="store_true",
    help="Output debugging information."
    )
parser.add_argument("-aap", "--advanced-audio-processing",
    action="store_true",
    help="Enable advanced audio processing. Use if you know what it does."
    )
parser.add_argument("-n", "--dry-run",
    action="store_true",
    help="Do a dry run."
    )

args = parser.parse_args()

def debug_output():
    #print(args)
    #args.input needs to check if there are two elements in list
    #print(len(os.path.splitext(args.input)))
    #print(os.path.splitext(args.input)[-1][1:])
    print()
    print("Output provided: " + str(output_provided))
    print("Output filename: " + output_filename)
    print("Input exists: " + str(input_exists))
    print("Output Exists: " + str(output_exists))
    print("Output Overwrite: " + str(args.overwrite))
    print("Intro exists: " + str(intro_exists))
    print("Outro exists: " + str(outro_exists))
    print("Logo exists: " + str(logo_exists))
    print("Intro Readable: " + str(intro_readable))
    print("Outro Readable: " + str(outro_readable))
    print("Logo Readable: " + str(logo_readable))
    print("Logo Margin Right: {}".format(args.logo_margin_right))
    print("Logo Margin Bottom: {}".format(args.logo_margin_bottom))
    print("Fade in duration: {}".format(args.fadein_duration))
    print("Fade out duration: {}".format(args.fadeout_duration))
    print("Output Video Bitrate: {}".format(args.bitrate))
    print("Output Audio Bitrate: {}".format(args.audio_bitrate))
    print("Advanced Audio Processing: {}".format(args.advanced_audio_processing))
    try:
        print("Input Video Size: {} x {}".format(w, h))
    except NameError:
        pass

    try:
        print("Intro Video Size: {} x {}".format(iw, ih))
    except NameError:
        pass

    try:
        print("outro Video Size: {} x {}".format(ow, oh))
    except NameError:
        pass

    try:
        print("Logo original size: {} x {}".format(logow, logoh))
    except NameError:
        pass

    try:
        print("Logo resized size: {} x {}".format(logorw, logorh))
    except NameError:
        pass

def do_exit(ret=0):
    if args.debug:
        debug_output()
    input("Press Enter to continue...")
    sys.exit(ret)

input_exists = os.path.exists(args.input)

intro_exists = os.path.exists(args.intro)
outro_exists = os.path.exists(args.outro)
logo_exists = os.path.exists(args.logo)

# ignore input ext as fudge for my habit of using mkv instead of MP4
output_ext = '.mp4'
# calculate Output...
output_filename = args.out
if output_filename:
    output_provided = True
    split_input = os.path.splitext(output_filename)
    if len(split_input) > 1:
        output_subname = "".join(split_input[:-1])
    else :
        # no functional difference
        output_subname = output_filename
    output_filename = output_subname + output_ext
else:
    output_provided = False
    split_input = os.path.splitext(args.input)
    if len(split_input) < 2:
        output_subname = args.input
    else :
        # ignore input ext as fudge for my habit of using mkv instead of MP4
        # no functional difference
        output_subname = "".join(split_input[:-1])
    output_filename = output_subname + ".output" + output_ext
output_exists = os.path.exists(output_filename)
input_readable = os.access(args.input, os.R_OK)
intro_readable = os.access(args.intro, os.R_OK)
outro_readable = os.access(args.outro, os.R_OK)
logo_readable = os.access(args.logo, os.R_OK)


if input_exists == False or input_readable == False:
    print()
    print("The input file '" + args.input + "' does not exist or is not readable. Please supply a readable input video.")
    do_exit(ret=1)

if output_exists == True and args.overwrite == False:
    print()
    print("The input file '" + output_filename + "' already exists. Use --overwrite, --output or -o to correct.")
    do_exit(ret=1)

output_list = []

input_video = VideoFileClip(args.input)
w,h = input_video.size

if intro_exists == True and intro_readable == True:
    intro_video = (VideoFileClip(args.intro)
        .fadein(args.intro_fadein_duration)
        .fadeout(args.intro_fadeout_duration)
        )
    iw,ih = intro_video.size
    if w != iw or h != ih:
        print()
        print("The intro video '{}' is not the same size as the input video.".format(args.intro))
        do_exit(ret=1)
    output_list.append(intro_video)

if logo_exists == True and logo_readable == True:
    logo = ImageClip(args.logo)
    logow,logoh = logo.size
    ratio = min(args.logo_size / logow, args.logo_size / logoh);
    logorw = math.ceil(logow * ratio)
    logorh = math.ceil(logoh * ratio)
    logo = (ImageClip(args.logo)
        .set_duration(input_video.duration)
        .resize(width=logorw, height=logorh)
        .margin(
            right=args.logo_margin_right,
            bottom=args.logo_margin_bottom,
            opacity=0
        )
        .set_position(('right', 'bottom'))
    )
    adjusted_input_video = CompositeVideoClip([input_video, logo])
else:
    adjusted_input_video = input_video

adjusted_input_video = (adjusted_input_video
    .fadein(args.fadein_duration)
    .fadeout(args.fadeout_duration)
    )
output_list.append(adjusted_input_video)

if outro_exists == True and outro_readable == True:
    outro_video = (VideoFileClip(args.outro)
        .fadein(args.outro_fadein_duration)
        .fadeout(args.outro_fadeout_duration)
        )
    ow,oh = outro_video.size
    if w != ow or h != oh:
        print()
        print("The outro video '{}' is not the same size as the input video.".format(args.outro))
        do_exit(ret=1)
    output_list.append(outro_video)

final_clip = concatenate_videoclips(output_list);

keyargs = {}
#keyargs['codec'] = 'libx264' # CPU encoding
keyargs['codec'] = 'h264_nvenc' # NVidia hardware acceleration,
keyargs['ffmpeg_params'] = [# '-crf', '20',
    '-b:v', str(args.bitrate),
    '-maxrate', str(args.bitrate),
    '-bufsize', str(args.bitrate * 2),
    ]
keyargs['audio_codec'] = 'aac'
# keyargs['audio_codec'] = 'libfdk_aac' # Fraunhofer FDK
keyargs['audio_bitrate'] = str(args.audio_bitrate)
# keyargs['audio_fps'] = '48000'
# keyargs['preset'] = 'fast'

if not args.dry_run:
    final_clip.write_videofile(output_filename, **keyargs)

do_exit()
