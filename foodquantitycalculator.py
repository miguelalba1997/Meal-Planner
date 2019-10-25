
import math

##here i take input from the user
protien = int(input('enter protien:'))
nprotien = 0
lprotien = protien
casien = 80

fat = int(input('enter fats:'))
nfat = 0
lfat = fat

carb = int(input('enter carbohydrates:'))
ncarb = 0
lcarb = carb

print('')

cal_total = (protien*4)+(carb*4)+(fat*9)
print('Total Calorie Intake:',cal_total,'Kcal')

print('')

##here i subtract constant macros from
##user input in order to make the calculations
##easier
protien = protien - 85.4
fat = fat - 5.07
carb = carb - 33

##here i organize a dictionary of foods i use in order
##to make it easier to work with. the value to each
##key is a list ordered: protien, fat, carb.
foodlist = {'tilapia':[21, 1.7, 0], 'salmon':[18, 13, 0], 'chicken':[31, 3.6, 0], 'casien':[80, 1.5, 6],
            'peanutbutter': [8, 16, 6], 'fishoil': [0, 100, 0], 'sweetpotato':[1.6, .1, 20], 'quinoa':[14.1, 6, 64],
            'oats': [2.4, 1.4, 12], 'spinach': [2.9, .4, 3]}

##here i access the dictionary in order to make
##initial calculations about the macros. i calculate
##the foods highest in carbs, then protien, then fats.

for k, v in foodlist.items():
  if k == 'quinoa':
    ncarb = carb/2
    qui_amount = ncarb/(v[2])
    if qui_amount < 1:
      qui_amount = qui_amount
    else:
      qui_amount = math.floor(qui_amount)
    carb = carb - ncarb
    protien = protien - (qui_amount)*(v[0])
    qui_fat = (v[1])*(qui_amount)
    fat = fat - qui_fat
    qui_amount = qui_amount*100
    print('Quinoa amount:', qui_amount,'g')

for k, v in foodlist.items():
  if k == 'sweetpotato':
    ncarb = carb/1.25
    sweet_amount = ncarb/(v[2])
    sweet_amount = math.floor(sweet_amount)
    carb = carb - ncarb
    protien = protien - (sweet_amount)*(v[0])
    sweet_fat = (v[1])*(sweet_amount)
    fat = fat - sweet_fat
    sweet_amount = sweet_amount*100
##  print('Sweet Potato amount:', sweet_amount,'g')
    
for k, v in foodlist.items():
  if k == 'salmon':
    nprotien = protien/2
    sal_amount = nprotien/(v[0])
    if sal_amount < 1:
      sal_amount = math.floor(sal_amount)
    if sal_amount > 2.25:
      sal_amount = 2.25
    else:
      sal_amount = sal_amount
    protien = protien - ((sal_amount)*(v[0]))
    sal_fat = (v[1])*(sal_amount)
    fat = fat - sal_fat
    sal_amount = sal_amount*100
    print('Salmon amount:',sal_amount,'g')

for k, v in foodlist.items():
  if k == 'chicken':
    nprotien = nprotien/2
    chick_amount = nprotien/(v[0])
    if chick_amount < 1:
      chick_amount = chick_amount
    else:
      chick_amount = math.floor(chick_amount)
    protien = protien - ((chick_amount)*(v[0]))
    chick_fat = (v[1])*(chick_amount)
    fat = fat - chick_fat
    chick_amount = chick_amount*100

for k, v in foodlist.items():
  if k == 'tilapia':
    nprotien = nprotien
    til_amount = nprotien/(v[0])
    til_amount = math.floor(til_amount)
    protien = protien - ((til_amount)*(v[0]))
    til_fat = (v[1])*(til_amount)
    fat = fat - til_fat
    til_amount = til_amount*100
    print ('Tilapia amount:',til_amount,'g')

for k, v in foodlist.items():
  if k == 'peanutbutter':
    if protien > v[0]:
      nut_amount = protien/v[1]
      protien = protien - (nut_amount)*(v[0])
      carb = carb - (nut_amount)*(v[1])
      fat = fat - (nut_amount)*(v[2])
      nut_amount = nut_amount*32
    else:
      nut_amount = fat/(v[2])
      protien = protien - (nut_amount)*(v[0])
      carb = carb - (nut_amount)*(v[1])
      fat = fat - (nut_amount)*(v[1])
      nut_amount = nut_amount*32
    print('Peanut Butter amount:', nut_amount,'g')
   
nprotien = protien
ncarb = carb
nfat = fat

##this corrects any over or underestimates in carbohydrate intake
if carb == 0:
  sweet_amount = sweet_amount
  print('Sweet Potato amount:', sweet_amount,'g')
  
if carb > 0:
  ncarb = carb/20
  carb = carb - ((ncarb)*20)
  fat = fat - ((ncarb)*.1)
  protien = protien - ((ncarb)*1.6)
  ncarb = ncarb*100
  sweet_amount = sweet_amount+ncarb
  print('Sweet Potato amount:', sweet_amount,'g')
 
if carb < 0:
  ncarb = carb/20
  carb = carb + ((ncarb)*20)
  fat = fat + ((ncarb)*.1)
  protien = protien + ((ncarb)*1.6)
  ncarb = ncarb*100
  sweet_amount = sweet_amount-ncarb
  print('Sweet Potato amount:', sweet_amount,'g')


##this corrects any underestimations in protien intake  
if protien == 0:
  chick_amount = chick_amount
  print('Chicken amount:',chick_amount,'g')
  
if protien > 0:
  nprotien = protien/31
  protien = protien - ((nprotien)*(31))
  fat = fat - ((nprotien)*3.6)
  nprotien = nprotien*100
  chick_amount = chick_amount + nprotien
  print('Chicken amount:',chick_amount,'g')

if protien < 0:
  nprotien = protien/31
  protien = protien +((nprotien)*(31))
  fat = fat + ((nprotien)*3.6)
  nprotien = nprotien*100
  chick_amount = chick_amount - nprotien
  print('Chicken amount:',chick_amount,'g')

nprotien = protien
ncarb = carb
nfat = fat
  

for k, v in foodlist.items():
  if k == 'fishoil':
    fish_amount = fat/(v[1])
    fat = fat - (fish_amount)*(v[1])
    fish_amount = fish_amount*100
    print('Fish Oil amount:', fish_amount,'g')

protien = abs(protien)
fat = abs(fat)
carb = abs(carb)

lprotien = lprotien+protien
lfat = lfat+fat
lcarb = lcarb+carb

print('Casien amount', casien,'g')

cal_total = (lprotien*4)+(lcarb*4)+(lfat*9)
print('')
print('Total Calorie Intake:',cal_total,'Kcal')
print('Protien:',lprotien)
print('Fat:',lfat)
print('Carbhydrates:',lcarb)
    
  
      
      
      
    
