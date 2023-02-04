from Driver import Driver
from time import sleep

driveTrain = Driver.getInstance()

while True:
    driveTrain.left()
    sleep(5)
    driveTrain.right()
    sleep(5)
