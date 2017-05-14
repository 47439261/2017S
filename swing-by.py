# -*- coding: utf-8 -*-
import numpy as np
import math

class Planet():
    def __init__(self,mass,init_x,init_y,orbital_period,radius):
        self.mass = mass
        self.init_x = init_x
        self.init_y = init_y
        self.orbital_period = orbital_period
        self.radius = radius
    
    def angular_vel(self):
        return 2*math.pi/self.orbital_period
    
    def coordinate(self,t):
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

    def init_coordinate(self):
        return np.array([self.init_x,self.init_y])

    def init_vel(self):
        return np.array([self.init_vel_x,self.init_vel_y])
    
    def velocity_grav(self,a,v,a_planet):
        return 0
    
    def coordinate_grav(self,a,v,a_planet):
        return 0

    def coordinate_non_grav(self,a,v):
        a += v * self.dt
        return a

mercury = Planet(10000,100,0,20,10)
venus = Planet(90000,200,0,40,20)
earth = Planet(10201,300,0,50,20)
mars = Planet(11111,400,0,60,20)
jupiter = Planet(1231323,500,0,70,20)
saturn = Planet(111111,600,0,80,20)
uranus = Planet(100000,700,0,90,20)
neptune = Planet(1222,800,0,120,20)
pluto = Planet(12222,900,0,150,20)



def planets_coordinates(t):
    return np.array([mercury.coordinate(t),venus.coordinate(t),earth.coordinate(t),mars.coordinate(t),jupiter.coordinate(t),saturn.coordinate(t),uranus.coordinate(t),pluto.coordinate(t)])

planets_coordinates = planets_coordinates(0)
voyager = Spacecraft(10.,10.,0.,5.,5.,0.1)
mark = 0
coordinate = np.zeros(2)




def main():
    distance_vector = planets_coordinates - a
    n = distance_vector.size
    distance_scl = np.zeros(n)
    for i in range(0,n):
        distance_scl[i] = (distance_vector[i][0]**2 + distance_vector[i][1]**2)**0.5
        mark = i
        if distance_scl[i]>3000000:
            distance_scl[i]=0
            mark = 0

    v = voyager.init_vel()
    for i in range(0,1000):
        if not mark=0:
            nearest_planet_coordinate = planets_coordinates[mark]
            coordinate = voyager.coordinate_grav(a,v,nearest_planet_coordinate)
            velocity = voyager.velocity_grav(a,v,nearest_planet_coordinate)
        else:
            coordinate = voyager.coordinate_non_grav
        judgement = judgement()
        
        #成功判定部分。judgement=0で続行、judgement=1で失敗、judgement=2で成功。
        if judgement = 1:
            print()
            break
        elif judgement = 2:
            print():
            break
        #上記の部分をjudge(judgement)とかでさらっと表したい。 

if __name__ == "__main__":

