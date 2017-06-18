import subprocess

tpl_path = 'desktop.tpl'
out_path = 'desktop.html'
picture_path = 'desktop.png'
quality = 50
width, height = 1920, 1080

fortune = subprocess.Popen(['fortune', '-a'], shell=True, stdout=subprocess.PIPE)
cow = subprocess.Popen(['cowsay', fortune.communicate()[0]], stdout=subprocess.PIPE)
cowsay = cow.communicate()[0]

with open(tpl_path, 'r') as f:
    tpl_content = f.read().replace('%cow%', cowsay)
    with open(out_path, 'w') as  outfile:
        outfile.truncate()
        outfile.write(tpl_content)

convert = subprocess.Popen(
    ['wkhtmltoimage', '--width', str(width), '--height', str(height), '--quality', str(quality), out_path,
     picture_path])
