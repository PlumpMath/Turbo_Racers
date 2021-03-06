from pandac.PandaModules import *
from direct.showbase.DirectObject import DirectObject
import random, sys, os, math
from Battledata import *
class Race(DirectObject):
    def __init__(self, environment, user, player1ship, player2ship):
        base.setBackgroundColor(0.666354238987, 0.960409045219, 1.0)
        environment.earth = loader.loadModel("canyon/world/cb")
        environment.earth.setZ(0.0)
        environment.earth.setScale(VBase3(5, 5, 5))
        environment.earth.setBin("background", 1)
        environment.ambientLight = AmbientLight("ambientLight")
        environment.ambientLight.setColor(Vec4(0.300000011921, 0.300000011921, 0.300000011921, 1))
        environment.directionalLight = DirectionalLight("directionalLight")
        environment.directionalLight.setDirection(Vec3(-5, -5, -5))
        environment.directionalLight.setColor(Vec4(1.0, 1.0, 1.0, 1))
        environment.directionalLight.setSpecularColor(Vec4(1.0, 1.0, 1.0, 1))
        environment.playerShip = Ship(player1ship, -113.0, -348.0, 5, 0.0, environment, 1)
        environment.player2Ship = Ship(player2ship, 326.0, 330.0, 5, 86.0, environment, 2)
        environment.powerups.append(Powerup(145.0, 304.0, 5))
        environment.powerups.append(Powerup(76.0, 429.0, 5))
        environment.powerups.append(Powerup(-82.0, 247.0, 5))
        environment.powerups.append(Powerup(-306.0, 206.0, 5))
        environment.powerups.append(Powerup(-445.0, 226.0, 5))
        environment.powerups.append(Powerup(-341.0, 395.0, 5))
        environment.powerups.append(Powerup(-441.0, 30.0, 5))
        environment.powerups.append(Powerup(-323.0, -365.0, 5))
        environment.powerups.append(Powerup(-215.0, -417.0, 5))
        environment.powerups.append(Powerup(-45.0, -237.0, 5))
        environment.powerups.append(Powerup(-56.0, -104.0, 5))
        environment.powerups.append(Powerup(202.0, -85.0, 5))
        environment.powerups.append(Powerup(337.0, -126.0, 5))
        environment.powerups.append(Powerup(256.0, -394.0, 5))
        environment.powerups.append(Powerup(452.0, -159.0, 5))
        environment.powerups.append(Powerup(412.0, 106.0, 5))
        base.camera.setPos(Point3(-113.428, -363.113, 9))
        environment.cam2.setPos(Point3(341.359, 329.387, 9))
