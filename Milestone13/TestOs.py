#bitte ebook seite 179-189 durcharbeiten:
# hierzu bitte das OS MOdul importieren und

# 1. euer Homeverzeichnis auflisten lassen,

import os
os.system('dir "C:\\"')


# 2. nur alle Verzeichnisse in eurem Homeverzeichnis auflisten lassen

import os
print(os.listdir())

# 3. euren Loginnamen/usernamen anzeigen lassen

import os
print(os.environ['USERPROFILE']) #C:\Users\username

# 4. die Betriebsystemart auflisten lassen

import os
print(os.name)

