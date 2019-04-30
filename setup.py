import pip
import utilities as utils

DEPENDENCES = ['serial', 'smbus', 'pyqt5', 'pyqtgraph']

def install(package):
    if(hasattr(pip, 'main')):
        pip.main(['install', package])
    elif(hasattr(pip, '__internal')):
        utils.log(0, 'No main class was found when trying to install ' + str(package) + 'switching to internal main.')
        pip.__internal.main(['install', package])

    utils.log(0, str(package) + ' package guarenteed installed.')

def main():
    for i in DEPENDENCES:
        install(i)

if __name__ == '__main__':
    main()
