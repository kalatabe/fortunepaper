import subprocess
import os

tpl_path = 'desktop.tpl'
out_path = 'desktop.html'
picture_path = 'desktop.png'
quality = 50
width, height = 1920, 1080

fortune = subprocess.Popen(['fortune', '-a'], shell=True, stdout=subprocess.PIPE)
cow = subprocess.Popen(['cowsay'], stdin=fortune.stdout, stdout=subprocess.PIPE)


with open(tpl_path, 'r') as f:
    tpl_content = f.read().replace('%cow%', cow.stdout.read())
    with open(out_path, 'w') as outfile:
		outfile.write(tpl_content)        

convert = subprocess.call(
    ['wkhtmltoimage', '--width', str(width), '--height', str(height), '--quality', str(quality), out_path,
     picture_path])

os.remove(out_path)
