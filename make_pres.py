import argparse
import os
import subprocess
import shutil

here = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("fname", help="Path to Notebook Presentation File")
args = parser.parse_args()

fpth = os.path.abspath(args.fname)
if not os.path.exists(fpth):
    raise IOError('{} does not exist'.format(fpth))

# make notebook html
cmd = "jupyter nbconvert {} --to slides --reveal-prefix=../reveal.js"
cmd = cmd.format(fpth)
fdir = os.path.dirname(fpth)
subprocess.check_call(cmd.split(), cwd=fdir)

# move it to index.html
bare = os.path.basename(fpth).split('.')[0]
oldhtml = os.path.join(fdir, '{}.slides.html'.format(bare))
newhtml = os.path.join(fdir, 'index.html')
shutil.move(oldhtml, newhtml)
