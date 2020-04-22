import time 
import pyautogui as py 
from PIL import Image
import numpy as np

print('start dino')
col = np.zeros(100)
birdup = np.zeros(100)
birddw = np.zeros(100)

py.keyUp('up')
py.keyUp('down')
start = time.time()
speedmode = 0
speed = -50
n_up = 0
mode = np.zeros(10)
while 1:
    t = time.time()
    # x,y = py.position()
    # col = py.pixel(x,y)
    # print(col)
    
    if n_up == 20 and mode[0] == 0 : 
        speed += 20
        mode[0] = 1
    if n_up == 40 and mode[1] == 0 :
        speed += 110
        mode[1] = 1
    if n_up == 50 and mode[2] == 0:
        speed += 100
        mode[2] = 1
    if n_up == 60 and mode[3] == 0:
        speed += 100
        mode[3] = 1
    if n_up == 65 and mode[4] == 0:
        speed += 90
        mode[4] = 1
    # if n_up == 70 and mode[5] == 0:
    #     speed += 30
    #     mode[5] = 1
    # if n_up == 75 and mode[6] == 0:
    #     speed += 30
    #     mode[6] = 1
    img = py.screenshot()
    for i in range(100):
        col_ = img.getpixel((450+i+speed,700))
        birdup_ = img.getpixel((360+i+speed,633))
        birddw_ = img.getpixel((360+i+speed,714))

        col[i] = col_[0]
        birdup[i] = birdup_[0]
        birddw[i] = birddw_[0]
    
    ni = img.getpixel((167,245))
    nightmode = ni[0] > 100
    if nightmode:
        tr = col[col < 200]
        bu = birdup[birdup < 200]
        bd = birddw[birddw < 200]
    else:
        tr = col[col > 100]
        bu = birdup[birdup > 100]
        bd = birddw[birddw > 100]

    if bu.size > 0  and bd.size == 0 :
        py.keyDown('down')
        print('down')
        time.sleep(0.2)
        py.keyUp('down')
        print(time.time()-t)
    elif tr.size > 0 :
        py.keyDown('up')
        n_up += 1
        print('up', n_up)
        py.keyUp('up')
        print(time.time()-t)
    
    #print(time.time()-t)
   

