from os import listdir, getcwd
from os.path import isfile, join
import hashlib
from time import time

from progress.bar import ShadyBar
from tnefparse.tnef import TNEF


def get_hash():
    h = hashlib.sha256()
    h.update(bytes(str(time()), encoding='utf-8'))
    return h.hexdigest()[:20]


all_files_list = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
dat_files_list = [f for f in all_files_list if '.dat' in f]

processed_files = []
ommited = []

bar = ShadyBar('Processing', max=len(dat_files_list))
for file in dat_files_list:
    t = TNEF(open(file, 'rb').read(), do_checksum=True)
    for i, a in enumerate(t.attachments):
        if '.pdf' in a.name.decode(encoding='utf-8'):
            if isfile(a.name):
                name = a.name.decode(encoding='utf-8')
                name = name.replace('.pdf', f'__{str(get_hash())}.pdf')
                with open(name, "wb") as afp:
                    afp.write(a.data)
                    processed_files.append(name)
            else:
                with open(a.name, "wb") as afp:
                    afp.write(a.data)
                    processed_files.append(a.name.decode(encoding='utf-8'))
        else:
            ommited.append(a.name.decode(encoding='utf-8'))
    bar.next()
bar.finish()

for item in ommited:
    print(f'Ommited: {item}')
