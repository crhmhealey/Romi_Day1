# code an instructions from this file here:
# https://choate.instructure.com/courses/10654/files/folder/Week%204?preview=2410137
from wpilib import TimedRobot, Joystick, Spark
from wpilib.drive import DifferentialDrive
import os
import wpilib

os.environ["HALSIMWS_HOST"] = "10.0.0.2"
os.environ["HALSIMWS_PORT"] = "3300"
# spark is for the motors... not spark motors but can be programmed with the same software

class MyRobot(TimedRobot):
    def robotInit(self):
        '''This method is called as the robot turns on and is often used to setup the
        joysticks and other presets.'''
        self.controller = Joystick(0)
        self.left_motor = Spark(0)
        self.right_motor = Spark(1) # left and right motor channels defined by romi
        self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)

    def robotPeriodic(self):
        '''This is called every cycle of the code. In general the code is loop
        through every .02 seconds.'''
        pass

    def autonomousInit(self):
        '''This is called once when the robot enters autonomous mode.'''
        pass

    def autonomousPeriodic(self):
        '''This is called every cycle while the robot is in autonomous.'''
        pass

    def teleopInit(self):
        '''This is called once at the start of Teleop.'''
        pass

    def teleopPeriodic(self):
        '''This is called once every cycle during Teleop'''
        forward = self.controller.getRawAxis(0)
        rotate = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, rotate)
    ### There are other methods that you can overwrite for when the robot is
    # disabled, or when the robot is in Test mode.