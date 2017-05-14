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

    def failure(self):
        print("◯◯に衝突しました。")


class Spacecraft():
    def __init__(self,mass,init_x,init_y,init_vel_x,init_vel_y,dt):
        self.mass = mass
        self.init_x = init_x
        self.init_y = init_y
        self.init_vel_x = init_vel_x
        self.init_vel_y = init_vel_y
        self.dt = dt

    def init_location(self):
        return np.array([self.init_x,self.init_y])

    def init_vel(self):
        return np.array([self.init_vel_x,self.init_vel_y])

    def location_grav(self,a,v,a_planet):
        return 0

    def location_non_grav(self,a,v):
        a += v * self.dt
        return a

def main():
    mercury = Planet()
    venus = Planet()
    earth = Planet()
    mars = Planet()
    jupiter = Planet()
    saturn = Planet()
    uranus = Planet()
    neptune = Planet()
    pluto = Planet()
    voyager = Spacecraft(10.,10.,0.,5.,5.,0.1)
    a = voyager.init_location()
    v = voyager.init_vel()
    for i in range(0,1000):
        if():
            a = voyager.location_grav(a,v,)
        else:
            a = voyager.location_non_grav
        judgement = judgement()
        
        #成功判定部分。judgement=0で続行、judgement=1で失敗、judgement=2で成功。
        if(judgement = 1):
            print()
            break
        elif(judgement = 2):
            print():
            break
        #上記の部分をjudge(judgement)とかでさらっと表したい。 

if __name__ == "__main__":
    earth = Planet(1000000,100,0,10)
    print earth.location(1231)
    for i in range(0,1000):
        a = voyager.location_non_grav(a,v)
        print a
