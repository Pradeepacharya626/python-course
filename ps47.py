            #DAY 14


FREEZING_POINT = 0
BOILING_POINT = 100
temperature = 12

def water_state(temperature):
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature > FREEZING_POINT and temperature < BOILING_POINT  :
        return "Liquid"
    elif temperature>BOILING_POINT:
        return "Gas"



print(water_state(temperature))

'''Here FREEZING_POINT and BOILING_POINT are Global variables
   hence these are accesed in def function also'''