# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: CLG_Lana.py
import pygame, random
Num_E = 0
Life = []
Pos_X = []
Pos_Y = []
Radium = []
Red = []
Green = []
Blue = []

def summon_Lana_Mud(True_Or_False, X, Y, R, RED, GREEN, BLUE):
    global Life
    global Num_E
    if True_Or_False == True:
        Num_E += 1
        Life.append(100)
        Pos_X.append(X)
        Pos_Y.append(Y)
        Radium.append(R)
        Red.append(RED)
        Blue.append(BLUE)
        Green.append(GREEN)
    else:
        None
    return


def Lana_Count():
    try:
        return Num_E
    except:
        None

    return


def Lana_Data_R(Num):
    try:
        return (
         Num, Life[Num], Pos_X[Num], Pos_Y[Num], Radium[Num], Red[Num], Green[Num], Blue[Num])
    except:
        None

    return


def Move_Lana(Num, VelY):
    try:
        for i in range(Num):
            Pos_Y[i] += VelY

    except:
        None

    return


def Kill_Lana(Num):
    global Num_E
    try:
        Num_E -= 1
        Life.pop(Num)
        Pos_X.pop(Num)
        Pos_Y.pop(Num)
        Radium.pop(Num)
        Green.pop(Num)
        Blue.pop(Num)
        Red.pop(Num)
    except:
        None

    return


def Damage_Lana(Num, Damage):
    try:
        Life[Num] = Life[Num] - Damage
    except:
        None

    return