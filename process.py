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

input_exists = os.path.exists(args.input)
if input_exists == False:
    print(args.input + ' does not exist or is not readable. Please supply a readable input video.')
    sys.exit(1)

outro_exists = os.path.exists(args.outro)
intro_exists = os.path.exists(args.intro)
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
    output_filename = output_path + output_subname + output_ext
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
intro_readable = os.access(args.intro, os.R_OK)
outro_readable = os.access(args.outro, os.R_OK)
logo_readable = os.access(args.logo, os.R_OK)

if args.debug:
    #print(args)
    #args.input needs to check if there are two elements in list
    #print(len(os.path.splitext(args.input)))
    #print(os.path.splitext(args.input)[-1][1:])

    print("Output provided: " + str(output_provided))
    print("Output filename: " + output_filename)
    print("Input exists: " + str(input_exists))
    print("Intro exists: " + str(intro_exists))
    print("Outro exists: " + str(outro_exists))
    print("Logo exists: " + str(logo_exists))
    print("Intro Readable: " + str(intro_readable))
    print("Outro Readable: " + str(outro_readable))
    print("Logo Readable: " + str(logo_readable))
    print("Output Exists: " + str(output_exists))

input("Press Enter to continue...")