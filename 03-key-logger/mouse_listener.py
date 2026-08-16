from pynput.mouse import Listener
def writetofile(x,y):
    with open("log.txt", 'a') as f:
        f.write("Mouse position on [0]".format(x,y))

with Listener(on_move=writetofile) as l:
    l.join()


