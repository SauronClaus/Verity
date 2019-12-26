from python_sagedining.sagedining.core import Sage, SageMenuItem, MenuCategory, Meal
#imports!
import datetime

sage_object = Sage("S0085")
#CA is S0085

sage_object.update()
#Need to update before use. 
MainIngredient = sage_object.get_categories_date(datetime.datetime.today(), Meal.LUNCH, [
    MenuCategory.MAIN_INGREDIENT,
    #Add as many of these as you want in this menu; use intellisense to determine which ones. Each one maps to a new sage dining category. 
])
PSIngredient = sage_object.get_categories_date(datetime.datetime.today(), Meal.LUNCH, [
    MenuCategory.PS,
])

for category in MainIngredient:
    for menu_item in category:
        print(f"Main: {str(menu_item)}")
#That one's main course
for category in PSIngredient:
    for menu_item in category:
        print(f"Dessert: {str(menu_item)}")
#This one's desert. 