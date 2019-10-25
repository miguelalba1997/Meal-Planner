#-------------------------------------------------------------------------------
# Name:        Cardio_calculator
# Purpose:
#
# Author:      Miguel
#
# Created:     31/1/2018
# Copyright:   (c) Miguel 2017
# Licence:     <THE SWOLEST>
#-------------------------------------------------------------------------------
import math 
import operator
# 	the purpose of this program is to give the user a rough estimate of how
#	many calories they're burning when doing low to medium intensity cardio.
time = int(input('please input the duration of your cardio in minutes: '))
wieght = int(input('please input your current body wieght in pounds:' ))

def cardio_calculator(time, wieght):	
	wieght = wieght/2.204 #	you want the wieght in kilograms
	time = time/60 #	you want the time in hours
	MET = 5 #	this is the difficulty of the excersice theres like a whole
			#	chart online look it up. this is actually an average of most 
			#	low - meadium intensity training. 
	cardio_Kcal = time * (wieght) * MET
	print('Total calories burned:', cardio_Kcal, ' Kcal')
	return 0


cardio_calculator(time, wieght)
