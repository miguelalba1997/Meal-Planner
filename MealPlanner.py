#-------------------------------------------------------------------------------
# Name:        MEAL PLANER
# Purpose:
#
# Author:      Miguel
#
# Created:     29/12/2017
# Copyright:   (c) Miguel 2017
# Licence:     <THE SWOLEST>
#-------------------------------------------------------------------------------
import math 
import operator

##    tilapia = [21, 1.7, 0]
##    salmon = [18, 13, 0]
##    chicken = [31, 3.6, 0]
##    casien = [73.5, 1.6, 6]
##    peanutbutter = [8, 16, 6]  per 32 grams
##    fishoil = [0, 100, 0]
##    sweetpotato = [2, .2, 20.7]
##    quinoa = [14.1, 6, 64]
##    oats = [2.4, 1.4, 12]
##    spinach = [2.9, 0, 3]
##    ground_beef = [17, 20, 0]
##    eggs = [6.3, 5, 0]    one large egg(50g)
##    ground_turkey = [18.7, 7, 0]
##    greek_yogurt = [10, 0, 4]
##    milk = [3.3, 2, 5]
##    white_potato = [2, .1, 17]
##    white_rice = [6, 0, 84] 
##    beans = [21.6, 1.4, 62.4]

def fat_calculator(protien, fat, carb, protien_amount, fat_amount, carb_amount, n, m, l):
	print('fats:')
	
	amount = [None]*m
	
	fat_meal_amount = fat_amount/m
	
	for i in range(m):
		amount[i] = fat_meal_amount/fat[i][1]
		if fat[i][1] == 16:
			pb_amount = amount[i] 
	
	for k in range(m):
		protien_amount = protien_amount - (amount[k]*fat[k][0])
		fat_amount = fat_amount - (amount[k]*fat[k][1])
		carb_amount = carb_amount - (amount[k]*fat[k][2])
	
	carb_amount1 = 0
	protien_amount1 = 0
	
	if carb_amount < -110 or protien_amount < -110:
		if protien_amount > carb_amount:
			protien_amount1 = (abs(protien_amount)) - 10
			new_amount = protien_amount1/8
			protien_amount = protien_amount + (new_amount*8)
			carb_amount = carb_amount + (new_amount*6)
			fat_amount = fat_amount + (new_amount *16)
			fish_oil_amount = fat_amount/100
			print('The amount of fish oil is ', fish_oil_amount*100, ' grams.')
			pb_amount = pb_amount - new_amount
		else:
			carb_amount1 = (abs(carb_amount)) - 10
			new_amount = carb_amount1/6
			protien_amount = protien_amount + (new_amount*8)
			carb_amount = carb_amount + (new_amount*6)
			fat_amount = fat_amount + (new_amount *16)
			fish_oil_amount = fat_amount/100
			print('The amount of fish oil is ', fish_oil_amount*100, ' grams.')
			pb_amount = pb_amount - new_amount

	for j in range(m):
		if fat[j][1] == 16:
			print('The amount of ', fat[j][3],' is ', pb_amount*32, ' grams.')
		else:
			print('The amount of ', fat[j][3],' is ', amount[j]*100, ' grams.')

#	we should include a loop that adds an extra amount of a carb source in just in case
#	theres any small amount of protien or carbs left over. maybe white potato would be a good candidate?
#	actually if the amount of carb is higher than protien pick rice, if vice versa pick greek yogurt.
	print(' ')
	print('the following are extra amounts of food to fill in the remaining macros:')
	if carb_amount > 0 or protien_amount > 0:
		if protien_amount > carb_amount:
			#print(protien_amount, carb_amount)
			extra_amount = protien_amount/10
			protien_amount = protien_amount - (extra_amount*10)
			carb_amount = carb_amount - (extra_amount*4)
			print('amount of greek yogurt is', extra_amount*100, ' grams.')
		elif carb_amount > protien_amount:
			if carb_amount < 22:
				#print(protien_amount, carb_amount)
				extra_amount = carb_amount/7
				carb_amount = carb_amount - (extra_amount*7)
				protien_amount = protien_amount - (extra_amount*1)
				print('amount of plain rice cakes is ', extra_amount*9, ' grams. (typical serving size is 9 grams)')
			else:
				#print(protien_amount, carb_amount)
				extra_amount = carb_amount/80
				carb_amount = carb_amount - (extra_amount*80)
				protien_amount = carb_amount - (extra_amount*7)
				print('amount of rice is ', extra_amount*100, ' grams.')
	
	print(' ')
	print('protien:',protien_amount, 'fat:', fat_amount, 'carb:', carb_amount)
	return 0

def protien_calculator(protien, fat, carb, protien_amount, fat_amount, carb_amount, n, m, l):
	print('protiens:')
#	first we need to the protien sorces based on highest sorce of 
#	protien since that is a priority 
	protien.sort(key=operator.itemgetter(0), reverse=True) 
	amount = [None]*n#	we need an empty array to store the amounts of 
					 #	the food sources in
	for k in range(len(protien)):
		if protien[k][0] == 73.5:
			protien_amount = protien_amount - 44
			fat_amount = fat_amount - 1.6
			carb_amount = carb_amount - 6
			del protien[k]
			print('The amount of  casien  is  2 scoops(60g).')
			break
		else:
			continue 			
	primary_source_amount = (.35*protien_amount)
#	since protien is pretty expensive and we want our protien sources to
#	come from leaner cuts so we want the majority of our protien comming from
#	the leanest option available if there are more than two options to choose from											
	
	protien_meal_amount0 = (protien_amount - primary_source_amount)/((len(protien))-1)#just dividing the protien up evenly amoung each choice
	protien_meal_amount1 = protien_amount/(len(protien))#	this is if we only have two options
	
#	print(protien_amount, primary_source_amount, protien_meal_amount0, protien_meal_amount1)
	
	for i in range(len(protien)):
		if n > 2:#	if we have more options we implement the above stated procedure
			amount[i] = protien_meal_amount0/protien[i][0]
			amount[0] = primary_source_amount/protien[0][0]
			if (protien[i][1]/protien[i][0]) > .53:#	we dont want too much of our fat to come from our protien
				if amount[i] > 2.2 and i != 0:#	if we have multiple choices to choose from right?
					amount[i] = 2.2#	This is typically a good amount no more than like 10% of our fat should come from this amount
		else:#	this is if we have only two choices.
			amount[i] = protien_meal_amount1/protien[i][0]
			if (protien[i][1]/protien[i][0]) > .53:#	now this might lowball the protien amount in diet with only fatty choices of protien
				if amount[i] > 2:#	but thats okay because that means that the diet is probably unrealistic
					amount[i] = 2
	
	for j in range(len(protien)):#	now we just update the fat and protien amounts. theres no carb calcultion here since protien has no carbs
		protien_amount = protien_amount - (amount[j]*protien[j][0])
		fat_amount = fat_amount - (amount[j]*protien[j][1])
		print('The amount of ', protien[j][3],' is ', amount[j]*100, ' grams.')
	print(' ')
	##print(protien_amount, carb_amount)
	
	fat_calculator(protien, fat, carb, protien_amount, fat_amount, carb_amount, n, m, l)
	return 0

#	in carb calculator we will pass the arguments option0, option1, 
#	option2, P, F, C and the amount of protien, fat, carb sources as protien, fat, carb, protien_amount, fat_amount,
#   carb_amount, one, two, three, respectively.

def carb_calculator(protien, fat, carb, protien_amount, fat_amount, carb_amount, n, m, l):
	print('Carbohydrates:')
#	we might want to sort the carb sorces based on highest sorce of 
#	carb if that is a priority. if it is the next line of code is helpful 	
#	carb.sort(key=operator.itemgetter(2), reverse=True)
	
	amount = [None]*l#	make an array to hold the amount of each carb source

#	interesting note in a 40/20/40 (p, f, c) split 60% of my fat came from
#	the 80% of non direct fat sources in my diet. in other words 3% of my 
#	protien and carb sources was made up of fat on average. 
#	so what ive done here is predicted that 3% of the total wieght of my non
#	fat source of food will be made up of fat on average and im taking that
#	percentage of the total amount of non fat macronutrient wieght and subracting
#	it from the total desired amount of fat. 
	for c in range(len(carb)):
		if carb[c][2] == 20:
			protien_amount = protien_amount - 12
			carb_amount = carb_amount - 56
			fat_amount = fat_amount - 4
			print('The amount of Arctic Zero is one container')
			del carb[c]
			break
	carb_amount1 = carb_amount
	predicted_fat_amount = fat_amount - ((carb_amount)*.03)# it might be a good idea to average the percent fat form carb sources and the precent fat from protien sources to best fit all diet types
	
#	we include an if statement that subtracts a variable amount of carbs 
#	from carb_amount to save it for the fat calculation in case the user picks 
#	a fat source with carbs in it. 
	for f in range(m):
		if fat[f][1] == 16 and m == 1:#	this relates strictly to peanut butter
			left_over = (predicted_fat_amount/16)*6
			carb_amount1 = carb_amount - left_over
			carb_meal_amount = carb_amount1/l
		else:
			carb_meal_amount = carb_amount1/l#	divide the amount of carb evenly
			continue					#	among the carbohydrate sources								
#	we want to make sure that we limit certain foods in a way that they 
#	dont end up providing significant source of protien or fat, as we 

#	want these macros to come from other food sources like meat and nuts
	for i in range(len(carb)):
		amount[i] = carb_meal_amount/carb[i][2]
		if carb[i][2] == 3:#	this is refering to spinach; its very
			if amount[i] > 4:#	volumous more than 400g is too much
				amount[i] = 4
				continue
		elif (carb[i][0])/(carb[i][2]) > .184:# this is to keep fat levels down
			if amount[i] > 1 and carb[i][2] != 67.5:#this is for carb sources high in fat/protien
				amount[i] = 1
			elif amount[i] > .6 and carb[i][2] == 67.5:#this is for oats since no one likes oats that much
				amount[i] = .6#	I just think that this a good amount of oats thats not too much
			else:
				continue
		else:
			continue
#	in this next step we need to keep track of the amount of protien and
#	fat provided from our carb sources so that that information can be
#	passed on to Protien_calculator and Fat_calculator when they need to
#	calculate the amount of protien and fat needed from each food source
	for k in range(len(carb)):
		protien_content = ((amount[k])*(carb[k][0]))
		protien_amount = protien_amount - protien_content
		fat_content = ((amount[k])*(carb[k][1]))
		fat_amount = fat_amount - fat_content
		carb_content = ((amount[k])*(carb[k][2]))
		carb_amount = carb_amount - carb_content

#	here we simply tell the user the amounts of food in grams need of 
#	each of the choices they made for thier carb source.
	for j in range(len(carb)):
		print('The amount of ', carb[j][3],' is ', amount[j]*100, 'grams.')
	print(' ')	
	protien_calculator(protien, fat, carb, protien_amount, fat_amount, carb_amount, n, m, l)
	
	return 0

def food_selection(P, F, C):
#    well we want to display a list of food options to the user
#    and have them choose a number of items from than list that
#    we will then use to calculate a meal plan.

    protienlist = [[20.3, 1.8, 0, 'Tilapia'], [18.6, 10.1, 0, 'Salmon'], [23, 2, 0, 'Chicken'], [73.5, 1.6, 6, 'Casien'], [17, 20, 0, 'Ground Beef'], [12.6, 10, 0, 'Eggs'], [18.7, 7, 0, 'Ground Turkey'], [10, 0, 4, 'Greek Yogurt'], [3.3, 2, 5, 'Milk'], [19.4, 14.1, 0, 'Top Sirloin Steak'], [22.9, 0, 0, 'Canned Tuna'], [21, 5, 0, 'Pork Loin']]

    fatlist = [[8, 16, 6, 'Peanut Butter'], [0, 100, 0, 'Fish Oil']]

    carblist = [[2, .2, 20.7, 'Sweet Potato'],[13.6, 5.7, 63.6, 'Quinoa'], [12.5, 7.5, 67.5, 'Oats'], [2.9, 0, 3, 'Spinach'], [2, .1, 18, 'White Potato'], [6, 0, 84, 'White Rice'], [21.6, 1.4, 62.4, 'Beans'], [25.8, 1.1, 60.1, 'Lentils'], [4.3, 1.4, 20, 'Arctic Zero']]

#   great now we have a food list that we can select from. The list
#   is organized 'protien, fat, carbs' in that order, measured in
#   grams uncooked and raw.
    print(' ')
    print('It is recomended that one of your choices be a fatty protien source(salmon, eggs, ground beef, steak).')
    print('')
    print('1.tilapia, 2.salmon, 3.chicken, 4.casien, 5.ground beef, 6.eggs, 7.ground turkey, 8.greek yogurt, 9.milk, 10. top sirloin steak, 11. canned tuna, 12. Pork loin')
    print(' ')

#   here we present the user with a list of protien sources, which will then
#   be used as later arguments

    N = int(input('Choose how many protien sources you want to have:'))

#   here were choosing not only the size of the array 'option0' but also
#   the limit of the for loop

    print('To choose a protien source type out the number of the protien source you would like:')

    option0 = [None]*N

    for x in range(N):
        print('Pick Option', x+1,':')
        i = int(input())#  this reads in information from the user
        option0[x] = protienlist[i-1]#   here we append the values the user enters
                                   #   into the list 'option'
        if i > 12:#  here it prevents the user from entering a wrong number
            print('please enter a different number')
            i = int(input('Enter Option Again:'))
            option0[x] = protienlist[i-1]
        else:
            continue
#-------------------------------------------------------------------------------
    print('1. peanut butter, 2. fish oil')
    print(' ')
#   here we present the user with a list of fat sources, which will then
#   be used as later arguments
    M = int(input('Choose how many fat sources you want to have:'))
#   here were choosing not only the size of the array 'option1' but also
#   the limit of the for loop
    print('To choose a fat source type out the number of the fat source you would like:')
    option1 = [None]*M #    this list stores the information for our fat sources

    for y in range(M):
        print('Pick Option', y+1,':')
        j = int(input())#  this reads in information from the user
        option1[y] = fatlist[j-1]#   here we append the values the user enters
                                  #   into the list 'option'
        if j > 2:#  here it prevents the user from entering a wrong number
            print('please enter a different number')
            j = int(input('Enter Option Again:'))
            option1[y] = fatlist[j-1]
        else:
            continue
#-------------------------------------------------------------------------------
    print('1.sweet potato, 2.quinoa, 3.oats, 4.spinach, 5.white potato, 6.white rice, 7.beans, 8.lentils, 9.Artic Zero(chunked/300 kcal)')
    print(' ')
#   here we present the user with a list of carb sources, which will then
#   be used as later arguments
    L = int(input('Choose how many carb sources you want to have:'))
#   here were choosing not only the size of the array 'option2' but also
#   the limit of the for loop
    print('To choose a carb source type out the number of the carb source you would like:')
    option2 = [None]*L #    this list stores the information for our carb sources

    for z in range(L):
        print('Pick Option', z+1, ':')
        k = int(input())#  this reads in information from the user
        option2[z] = carblist[k-1]#   here we append the values the user enters
                                  #   into the list 'option'
        if k > 9:#  here it prevents the user from entering a wrong number
            print('please enter a different number')
            k = int(input('Enter Option Again:'))
            option2[z] = carblist[k-1]
        else:
            continue
    carb_calculator(option0, option1, option2, P, F, C, N, M, L)
#	the reason why i don't call each function in this functon is because
#	i want the functions to be executed in a certain order. for example 
#	carbohydrates should go first since it has the most amount of 
#	influence over the amount of other macronutrients when the amount of
#	food is calculated. 
    return 0

def macro_selection():
	print('First enter the amount of desired daily macronutrients in grams')
#	this reads in the amount of protien fat and carb desired in grams
	protiens = int(input('enter grams of protien:'))
	fats = int(input('enter grams of fats:'))
	carbs = int(input('enter grams of carbohydrates:'))
	
	food_selection(protiens, fats, carbs)#	pass in the amount of macros
										 #	in grams 
	
	return 0
#	macro_selection acts like my main function 
macro_selection()
