"""
an app that does lots of stuff
"""
import math
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT

class Converter(toga.App):
    def total_calories(self):
        return str(math.ceil(4*(self.protien + self.carb) + 9*self.fat)) + '  Kcal'

    def adjustments(self):
        ##this corrects any over or underestimates in carbohydrate intake
        if self.carb == 0:
          self.sweet_amount.value = str(float(self.sweet_amount.value)) + 'g'
        
        if self.carb > 0:
          self.ncarb = self.carb/20
          self.carb = self.carb - ((self.ncarb)*20)
          self.fat = self.fat - ((self.ncarb)*.1)
          self.protien = self.protien - ((self.ncarb)*1.6)
          self.ncarb = self.ncarb*100
          self.sweet_amount.value = str(float(self.sweet_amount.value) + self.ncarb) + 'g'
                   
        if self.carb < 0:
          self.ncarb = self.carb/20
          self.carb = self.carb + ((self.ncarb)*20)
          self.fat = self.fat + ((self.ncarb)*.1)
          self.protien = self.protien + ((self.ncarb)*1.6)
          self.ncarb = self.ncarb*100
          self.sweet_amount.value = str(float(self.sweet_amount.value) - self.ncarb) + 'g'
        
        ##this corrects any underestimations in protien intake  
        if self.protien == 0:
          self.chicken_amount.value = self.chicken_amount.value + 'g'
                    
        if self.protien > 0:
          self.nprotien = self.protien/31.
          self.protien = self.protien - ((self.nprotien)*(31.))
          self.fat = self.fat - ((self.nprotien)*3.6)
          self.nprotien = self.nprotien*100
          self.chicken_amount.value = str(float(self.chicken_amount.value) + self.nprotien) + 'g'
          
        if self.protien < 0:
          self.nprotien = self.protien/31.
          self.protien = self.protien +((self.nprotien)*(31.))
          self.fat = self.fat + ((self.nprotien)*3.6)
          self.nprotien = self.nprotien*100
          self.chicken_amount.value = str(float(self.chicken_amount.value) - self.nprotien) + 'g'
          
        self.nprotien = self.protien
        self.ncarb = self.carb
        self.nfat = self.fat
        
        self.lprotien = self.lprotien + abs(self.protien)
        self.lfat = self.lfat + abs(self.fat)
        self.lcarb = self.lcarb + abs(self.carb)

        self.protien = self.lprotien
        self.fat = self.lfat
        self.carb = self.lcarb
        
    def MealPlanner(self):
        ##here i subtract constant macros from
        ##user input in order to make the calculations
        ##easier   
        self.nprotien = 0
        self.nfat = 0
        self.ncarb = 0

        self.lprotien = self.protien
        self.lcarb = self.carb
        self.lfat = self.fat 

        self.protien -= 85.4
        self.fat -= 5.07
        self.carb -= 33.0
        
        ##here i organize a dictionary of foods i use in order
        ##to make it easier to work with. the value to each
        ##key is a list ordered: protien, fat, carb.
    
        foodlist = {'tilapia':[21, 1.7, 0], 'salmon':[18, 13, 0], 'chicken':[31, 3.6, 0], 'casien':[80, 1.5, 6],
                    'peanutbutter': [8, 16, 6], 'fishoil': [0, 100, 0], 'sweetpotato':[1.6, .1, 20], 'quinoa':[14.1, 6, 64],
                    'oats': [2.4, 1.4, 12], 'spinach': [2.9, .4, 3]}
        
        ##here i access the dictionary in order to make
        ##initial calculations about the macros. i calculate
        ##the foods highest in carbs, then protien, then fats.
        
        for k, v in foodlist.items():#get amount of quinoa
          if k == 'quinoa':
            self.ncarb = self.carb/2
            qui_amount = self.ncarb/(v[2])
            if qui_amount < 1:
              qui_amount = qui_amount
            else:
              qui_amount = math.floor(qui_amount)
            self.carb -= self.ncarb
            self.protien -= (qui_amount)*(v[0])
            qui_fat = (v[1])*(qui_amount)
            self.fat -= qui_fat
            qui_amount *= 100
        self.qui_amount.value = str(qui_amount) + 'g'

        for k, v in foodlist.items():#get amount of sweet potato
          if k == 'sweetpotato':
            self.ncarb = self.carb/1.25
            sweet_amount = self.ncarb/(v[2])
            sweet_amount = math.floor(sweet_amount)
            self.carb -= self.ncarb
            self.protien -= (sweet_amount)*(v[0])
            sweet_fat = (v[1])*(sweet_amount)
            self.fat -= sweet_fat
            sweet_amount = sweet_amount*100 
        self.sweet_amount.value = sweet_amount

        for k, v in foodlist.items():#get amount of salmon
          if k == 'salmon':
            self.nprotien = self.protien/2
            sal_amount = self.nprotien/(v[0])
            if sal_amount < 1:
              sal_amount = math.floor(sal_amount)
            if sal_amount > 2.25:
              sal_amount = 2.25
            else:
              sal_amount = sal_amount
            self.protien -= ((sal_amount)*(v[0]))
            sal_fat = (v[1])*(sal_amount)
            self.fat -= sal_fat
            sal_amount = sal_amount*100
        self.salmon_amount.value = str(sal_amount) + 'g'

        for k, v in foodlist.items():#get amount of chicken
          if k == 'chicken':
            self.nprotien = self.nprotien/2
            chick_amount = self.nprotien/(v[0])
            if chick_amount < 1:
              chick_amount = chick_amount
            else:
              chick_amount = math.floor(chick_amount)
            self.protien = self.protien - ((chick_amount)*(v[0]))
            chick_fat = (v[1])*(chick_amount)
            self.fat -= chick_fat
            chick_amount = chick_amount*100
        self.chicken_amount.value = chick_amount

        for k, v in foodlist.items():#get amount of tilapia
          if k == 'tilapia':
            self.nprotien = self.nprotien
            til_amount = self.nprotien/(v[0])
            til_amount = math.floor(til_amount)
            self.protien -= ((til_amount)*(v[0]))
            til_fat = (v[1])*(til_amount)
            self.fat -= til_fat
            til_amount *= 100
        self.tilapia_amount.value = str(til_amount) + 'g'
        
        for k, v in foodlist.items():
          if k == 'peanutbutter':
            if self.protien > v[0]:
              nut_amount = self.protien/v[1]
              self.protien -= (nut_amount)*(v[0])
              self.carb -= (nut_amount)*(v[1])
              self.fat -= (nut_amount)*(v[2])
              nut_amount = nut_amount*32
            else:
              nut_amount = self.fat/(v[2])
              self.protien -= (nut_amount)*(v[0])
              self.carb -= (nut_amount)*(v[1])
              self.fat -= (nut_amount)*(v[1])
              nut_amount = nut_amount*32
        self.nut_amount.value = str(nut_amount) + 'g'
 
        #self.adjustments()        

    def calculate(self, widget):
        #try:
        #set up the variables for our macronutrients we're keeping 
        #two sets of variables to keep track of how many grams of 
        #fat we are actually getting vs how much we wanted originally
        self.protien = float(self.protien_input.value) 
        self.fat = float(self.fat_input.value)
        self.carb = float(self.carbs_input.value)
        
        #calculate total number of calories we initially asked for   
        self.calories_input.value = self.total_calories()
        self.MealPlanner()
        self.adjustments()   
        self.final_calories.value = self.total_calories()
        """
        except Exception:
            self.calories_input.value = '???'
            self.qui_amount.value = '???'
            self.sweet_amount.value = '???'   
            self.salmon_amount.value = '???'
            self.chicken_amount.value = '???'
            self.tilapia_amount.value = '???'
            self.nut_amount.value = '???'
            self.final_calories.value = '???'
        """
    def startup(self):
        # Create a main window with a name matching the app
        self.main_window = toga.MainWindow(title=self.name)

        # Create a main content box and mini input and output boxes
        carbs_box = toga.Box()
        protien_box = toga.Box()
        fat_box = toga.Box()
        calories_box = toga.Box()
        quinoa_box = toga.Box()        
        sweet_box = toga.Box()
        salmon_box = toga.Box()
        chicken_box = toga.Box()
        tilapia_box = toga.Box()    
        nut_box = toga.Box()
        final_box = toga.Box()

        box = toga.Box()

        #setup out input and output variables
        self.protien_input = toga.TextInput()
        self.carbs_input = toga.TextInput()
        self.fat_input = toga.TextInput()        
        self.calories_input = toga.TextInput(readonly = True)        
        self.qui_amount = toga.TextInput(readonly = True)
        self.sweet_amount = toga.TextInput(readonly = True)
        self.salmon_amount = toga.TextInput(readonly = True)
        self.chicken_amount = toga.TextInput(readonly = True)
        self.tilapia_amount = toga.TextInput(readonly = True)
        self.nut_amount = toga.TextInput(readonly = True)
        self.final_calories = toga.TextInput(readonly = True)

        #create the labels for our input and output boxes
        self.fat_label = toga.Label('Fat', style=Pack(text_align=RIGHT))
        self.carbs_label = toga.Label('Carb', style=Pack(text_align=RIGHT))
        self.protien_label = toga.Label('Protien', style=Pack(text_align=RIGHT))
        self.calories_label = toga.Label('Total Calories', style=Pack(text_align = RIGHT))
        self.quinoa_label = toga.Label('Quinoa amount', style=Pack(text_align = RIGHT))
        self.sweet_label = toga.Label('Sweet Potato \namount', style=Pack(text_align = RIGHT))
        self.salmon_label = toga.Label('Salmon amount', style=Pack(text_align = RIGHT))
        self.chicken_label = toga.Label('Chicken amount', style=Pack(text_align = RIGHT))
        self.tilapia_label = toga.Label('Tilapia amount', style=Pack(text_align = RIGHT))
        self.nut_label = toga.Label('Peanut Butter \namount', style=Pack(text_align = RIGHT))
        self.final_label = toga.Label('Actual Calories \nPer Day', style=Pack(text_align = RIGHT))

        #create our calculate button
        button = toga.Button('Create Meal Plan', on_press=self.calculate)

        #add the labels and input methods to our boxes
        carbs_box.add(self.carbs_label)
        carbs_box.add(self.carbs_input)
        
        protien_box.add(self.protien_label)
        protien_box.add(self.protien_input)
        
        fat_box.add(self.fat_label)
        fat_box.add(self.fat_input)
        
        calories_box.add(self.calories_label)
        calories_box.add(self.calories_input)
        
        quinoa_box.add(self.quinoa_label)
        quinoa_box.add(self.qui_amount)
        
        sweet_box.add(self.sweet_label)
        sweet_box.add(self.sweet_amount)
        
        salmon_box.add(self.salmon_label)
        salmon_box.add(self.salmon_amount)
        
        chicken_box.add(self.chicken_label)
        chicken_box.add(self.chicken_amount)
        
        tilapia_box.add(self.tilapia_label)
        tilapia_box.add(self.tilapia_amount)
        
        nut_box.add(self.nut_label)
        nut_box.add(self.nut_amount)
        
        final_box.add(self.final_label)
        final_box.add(self.final_calories)

        #add the boxes into our main box
        box.add(carbs_box)
        box.add(protien_box)
        box.add(fat_box)
        box.add(button)
        box.add(calories_box)
        box.add(quinoa_box)
        box.add(sweet_box)        
        box.add(salmon_box)
        box.add(chicken_box)
        box.add(tilapia_box)
        box.add(nut_box)
        box.add(final_box)
        
        box.style.update(direction=COLUMN, padding_top=100)
        carbs_box.style.update(direction=ROW, padding=5)
        protien_box.style.update(direction=ROW, padding=5)
        fat_box.style.update(direction=ROW, padding=5)
        calories_box.style.update(direction=ROW, padding=5)
        quinoa_box.style.update(direction=ROW, padding=5)
        sweet_box.style.update(direction=ROW, padding=5)
        salmon_box.style.update(direction=ROW, padding=5)
        chicken_box.style.update(direction=ROW, padding=5)
        tilapia_box.style.update(direction=ROW, padding=5)
        nut_box.style.update(direction=ROW, padding=5)
        final_box.style.update(direction=ROW, padding=5)        

        self.protien_input.style.update(flex=1, padding_right = 20)
        self.carbs_input.style.update(flex=1, padding_right=20)
        self.fat_input.style.update(flex=1, padding_right=20)
        self.calories_input.style.update(flex=1, padding_right=20)
        self.qui_amount.style.update(flex=1, padding_right=20)
        self.sweet_amount.style.update(flex=1, padding_right=20)
        self.salmon_amount.style.update(flex=1, padding_right=20)
        self.chicken_amount.style.update(flex=1, padding_right=20)
        self.tilapia_amount.style.update(flex=1, padding_right=20)
        self.nut_amount.style.update(flex=1, padding_right=20)
        self.final_calories.style.update(flex=1, padding_right=20)

        self.protien_label.style.update(width=120, padding_right=20)
        self.carbs_label.style.update(width=120, padding_right=20)
        self.fat_label.style.update(width=120, padding_right=20)
        self.calories_label.style.update(width=120, padding_right=20)
        self.quinoa_label.style.update(width=120, padding_right=20)
        self.sweet_label.style.update(width=120, padding_right=20) 
        self.salmon_label.style.update(width=120, padding_right=20) 
        self.chicken_label.style.update(width=120, padding_right=20)
        self.tilapia_label.style.update(width=120, padding_right=20)
        self.nut_label.style.update(width=120, padding_right=20)
        self.final_label.style.update(width=120, padding_right=20)

        button.style.update(padding=20, flex=1)

        # Add the content on the main window
        self.main_window.content = box

        # Show the main window
        self.main_window.show()


def main():
    return Converter('Converter', 'org.pybee.converter')
