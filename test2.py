from svgtrace import trace
from pathlib import Path

# get the base directory 
THISDIR = str(Path(__file__).resolve().parent)

# prepare the output .svg file
bw = open(THISDIR + "/result.svg", "w")
# convert the input image bitmap to svg
bw.write(trace(THISDIR + "/input.png", True))
bw.close()