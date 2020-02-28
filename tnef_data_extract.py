"""
Extracts PDF file form DAT files and saves them
"""
from os import listdir, getcwd
from os.path import isfile, join
import hashlib
from time import time

from progress.bar import ShadyBar
from tnefparse.tnef import TNEF


def get_hash():
    """
    Hashing method for filename uniques
    :return: str
    """
    hashed_filename = hashlib.sha256()
    hashed_filename.update(bytes(str(time()), encoding='utf-8'))
    return hashed_filename.hexdigest()[:20]


ALL_FILES_LIST = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
DAT_FILES_LIST = [f for f in ALL_FILES_LIST if '.dat' in f]

PROCESSED_FILES = []
OMITTED_FILES = []

bar = ShadyBar('Processing', max=len(DAT_FILES_LIST))
for file in DAT_FILES_LIST:
    t = TNEF(open(file, 'rb').read(), do_checksum=True)
    for i, a in enumerate(t.attachments):
        if '.pdf' in a.name.decode(encoding='utf-8'):
            if isfile(a.name):
                name = a.name.decode(encoding='utf-8')
                name = name.replace('.pdf', f'__{str(get_hash())}.pdf')
                with open(name, "wb") as afp:
                    afp.write(a.data)
                    PROCESSED_FILES.append(name)
            else:
                with open(a.name, "wb") as afp:
                    afp.write(a.data)
                    PROCESSED_FILES.append(a.name.decode(encoding='utf-8'))
        else:
            OMITTED_FILES.append(a.name.decode(encoding='utf-8'))
    bar.next()
bar.finish()

for item in OMITTED_FILES:
    print(f'Ommited: {item}')
