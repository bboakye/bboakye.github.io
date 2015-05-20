from gopigo import
import time
import math
set_speed(100)

def move_forward(feet):
    mm=feet*304.8
    steps= int(mm/11.34464014)
    time.sleep(.1)
    enc_tgt(1,1,steps)
    fwd()
    time.sleep(3)
    
def move_right():  
    time.sleep(.1)
    enc_tgt(1,0,14)
    right()
    time.sleep(3)
    
 def move_left():
    time.sleep(.1)
    enc_tgt(0,1,14)
    left()
    time.sleep(3)

move_forward(4)
move_right(2)
