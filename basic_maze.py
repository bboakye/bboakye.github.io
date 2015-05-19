from gopigo import
import time
import math
set_speed(0-255)
enc_tgt(1,1,18)
time.sleep(.1)
fwd()
time.sleep(3)
def move_forward(feet):
    mm=feet*304.8
    steps= mm/11.34464014
