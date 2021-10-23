import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.Series({"№ Микрорайона": 17 })

koll_mikro=int(input("Введите колличество микро-районов"))

while koll_mikro!=0:
    koll_mikro-=1
    name_mikro = input("Введите номер микрорайона: ")
    distance=int(input('Протяжённость дороги микрорайона: '))
    snow_cover=int(input('Введите процентную заснеженность дорог: '))
    speed=10


    if snow_cover<=33: #1
        if snow_cover in range(0,9):
            speed=10
        elif snow_cover in range(9,18):
            speed-=1
        elif snow_cover in range(18,27):
            speed -= 2
        else:
            speed -= 3
    elif snow_cover<=66: #2
        if snow_cover in range(34,44):
            speed-=4
        elif snow_cover in range(44,54):
            speed-=5
        elif snow_cover in range(54,64):
            speed -=6
        else:
            speed -=7
    elif snow_cover<=100: #3
        if snow_cover in range(66,76):
            speed-=8
        elif snow_cover in range(76,86):
            speed-=9
        elif snow_cover in range(86,96):
            speed -=9,4
        else:
            speed -=9,4
    time=distance/speed;
    print()


#не рабит(((((((((((9 не доделан