from application.salary import *
from application.db.people import *
from datetime import *
import matplotlib.pyplot as mat #Импорт со звездочкой невозможен

def hedgehog_chart(x, y):
    mat.plot(x, y, marker='*', linestyle='-.')
    mat.title('График популяции ежей')
    mat.xlabel('количество')
    mat.ylabel('год')
    mat.show()


if __name__ == '__main__':
    print(f'Текущая дата и время: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')

    calculate_salary()

    get_employees()

    hedgehog_chart([2011, 2012, 2013, 2014, 2015], [100000, 90000, 95000, 105000, 98000])

