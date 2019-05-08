import sys
from argparse import ArgumentParser
from moviepy.editor import *

parser = ArgumentParser(description="""
Process a video file, optionally adding a logo, an intro and an outro.
    """)
parser.add_argument("input", help="The video file to process.")
parser.add_argument("--intro", 
    default="intro.mp4", 
    help="The intro video file to use. By default, 'intro.mp4' is used."
    )
parser.add_argument("--outro",
    default="outro.mp4",
    help="The outro file to use. By default, 'outro.mp4' is used."
    )
parser.add_argument("--logo",
    default="logo.png",
    help="The outro file to use. By default, 'outro.mp4' is used."
    )
parser.add_argument("-o", "--out",
    help="The output filename. By default, this is the input file plus '.output'. Example 'input.output.mp4'"
    )
parser.add_argument("-d", "--debug", 
    action="store_true", 
    help="Output debugging information."
    )

args = parser.parse_args()
if args.debug:
    print(args)

input_exists = os.path.exists(args.input)
if input_exists == False:
    print(args.input + ' does not exist or is not readable. Please supply a readable input video.')
    sys.exit(1)

intro_exists = os.path.exists(args.intro)
outro_exists = os.path.exists(args.outro)
logo_exists = os.path.exists(args.logo)

intro_readable = os.access(args.intro, os.R_OK)
outro_readable = os.access(args.outro, os.R_OK)
logo_readable = os.access(args.logo, os.R_OK)

input("Press Enter to continue...")