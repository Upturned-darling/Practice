

import wpilib


class myrobot(wpilib.samplerobot):
  '''Main Robot Class'''
  
  def robotInit(self):
    '''Initialization code here'''
    
    self.lstick = wpilib.joystick(1)
    self.motor = wpilib.jaguar(8)

def disabled(self)
while self.is disabled():
  wpilib.timer.delay(0.01)
  
  def autonomous(self)
  
  while self.isAutonomous() and self.isEnabled()
  wpilib.timer.delay(0.01)
  def operatorcontrol(self)
  
  timer = wpilib.timer()
  timer.start()
  
