# -*- coding: utf-8 -*-
import numpy as np
import math

class Planet():
    def __init__(self,mass,init_x,init_y,orbital_period):
        self.mass = mass
        self.init_x = init_x
        self.init_y = init_y
        self.orbital_period = orbital_period
    
    def angular_vel(self):
        return 2*math.pi/self.orbital_period
    
    def location(self,t):
        radius = (self.init_x**2 + self.init_y**2)**0.5
        init_theta = np.arcsin(self.init_y / radius)
        angular_vel = self.angular_vel()
        theta = init_theta + t * angular_vel
        location = np.array([radius*np.cos(theta),radius*np.sin(theta)])
        return location
    
    def distance(self,x_sp,y_sp,t):
        return 0


class Spacecraft():
    def __init__(self,mass):
        self.mass = mass

if __name__ == "__main__":
    earth = Planet(1000000,100,0,10)
    print earth.location(1231)
