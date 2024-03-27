import platform
import os
if str(platform.system()) == 'Windows':
    has_windows = True
else:
    has_windows = False
if not has_windows:   
    print('You do not have the reccomended OS for this program. Some features may work incorrectly.')
    os.system('python3 -m pip install playsound==1.2.2')
    os.system('python3 -m pip install requests')
    os.system('python3 -m pip install keyboard')
    os.system('python3 -m pip install termcolor')
    os.system('python3 -m pip install packaging')
    os.system('python3 -m pip install pytube')
    os.system('python3 -m pip install psutil')
    os.system('python3 -m pip install awesome-progress-bar')
    os.system('python3 -m pip install pynput')
else:
    os.system('py -m pip install playsound==1.2.2')
    os.system('py -m pip install requests')
    os.system('py -m pip install keyboard')
    os.system('py -m pip install termcolor')
    os.system('py -m pip install packaging')
    os.system('py -m pip install pytube')
    os.system('py -m pip install psutil')
    os.system('py -m pip install awesome-progress-bar')
    os.system('py -m pip install pynput')
input('All Finished! Press enter to complete source-code setup')
