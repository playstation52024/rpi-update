from os import system as sys
from os import remove as rm
from time import sleep as s
# Ask the user to supply a Raspbian codename
print('Please enter the codename for the version of Raspbian you want to install:')
codename = input('>>> ')

sys('sudo su')
# Switch repositories
print('Switching repositories...')
with open ('/etc/apt/sources.list', 'w') as f:
    f.write('deb https://raspbian.raspberrypi.org/raspbian/ ' + codename + ' main contrib non-free rpi')
    f.write('# Uncomment line below then \'apt-get update\' to enable \'apt-get source\'')
    f.write('#deb- src https://raspbian.raspberrypi.org/raspbian/ ' + codename + 'main contrib non-free rpi')
print('Repositories switched successfully.')

# Update
print('Updating...')
sys('sudo apt update')
sys('sudo apt upgrade')

# Reboot
print('Rebooting in 5 sec...')
s(5)
print('Rebooting now...')
sys('sudo reboot')
