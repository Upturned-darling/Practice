

import wpilib


class myrobot(wpilib.samplerobot):
  '''Main Robot Class'''
  
  def robotInit(self):
    '''Initialization code here'''
    
    self.lstick = wpilib.joystick(1)
    self.motor = wpilib.jaguar(8)
