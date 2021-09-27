from libsoundtouch import soundtouch_device
from threading import Timer
import os

out_of_time=False








device = soundtouch_device('10.1.1.21')  # Manual configuration
device.power_on()

device.select_source_aux()
volume = device.volume()

# Config object
print(f'Device : {device.config.name}')
print(f'Current Volume : {volume.actual}')
print(f"Is Muted? {volume.muted}")

print('\n')
print('***************************')





def time_ran_out():
    print("Setting Defaults")
    device.set_volume(40)
    out_of_time=True
    t.cancel()    
    os._exit(0)



t=Timer(3,time_ran_out)
t.start()

vol_amount = input("Set Volume to: ")

if vol_amount !=None and not out_of_time:
    device.set_volume(vol_amount)
    print("Input given")
    t.cancel()
