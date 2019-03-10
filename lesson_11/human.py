class Human:
    def __init__(self, new_name="Аноним"):
        # Сначала хотел дать дефолтное имя "Господин Никто"
        # Но отсылка к Двачу показалась забавнее
        self.__name = new_name
        print("Родился человек по имени {0}".format(new_name))
        self.Q = {0:"(нет)",1:"плохо",2:"нормально",3:"хорошо",4:"отлично"}
        self.__eat = 100
        self.__sleep = 100
        self.__rest = 100
        self.__money = 10
        self.__age = 0
        self.__treads = 0
        self.__alive = True
    
    def lost_passport(self, new_name="Аноним"):
        print("{0} потерял паспорт и восстановил его под именем {1}".format(self.__name, new_name))
        self.__name = new_name
    
    def eating(self, food=2):
        if food > 4:
            food = 4
        while food*3 > self.__money:
            food -= 1
        if food < 0:
            food = 0
        print(self.__name+" ест "+self.Q[food])
        self.__eat += food * 5
        if self.__eat > 300:
            self.__eat = 300
        self.__money -= food * 3

    def sleeping(self, nights=2):
        if nights > 4:
            nights = 4
        elif nights < 0:
            nights = 0
        print(self.__name+" спит "+self.Q[nights])
        self.__sleep += nights * 10
        if self.__sleep > 100:
            self.__sleep = 100
        self.__rest += nights * 2
        if self.__rest > 100:
            self.__rest = 100
        self.__eat -= 3
        
    def working(self, days=5):
        if self.__age < 18:
            # Родители дали денег на обед
            self.__money += 3
        elif self.__age >= 65:
            # Платят пенсию
            self.__money += 4
            print("{0} на пенсии".format(self.__name))
        else:
            if days > 7:
                days = 7
            elif days < 0:
                days = 0
            print("{0} работает {1} дней в неделю".format(self.__name, days))
            self.__rest -= days * 3
            if self.__rest < 0:
                self.__sleep += self.__rest
                self.__rest = 0
            self.__money += days * (80*self.__age - self.__age*self.__age)/800
        
    def relaxing(self, t=2):
        if t > 5:
            t = 5
        elif t < 0:
            t = 0
        print(self.__name+" отдыхает "+self.Q[t]+": "+str(t)+" тредов Двача прочитано")
        self.__treads += t
        self.__rest += t * 2
        self.__eat -= 1
        
    def growing(self):
        self.__age += 1
        self.__eat -= 3
        self.__sleep -= 20
        print("{0} празднует день рождения".format(self.__name))
    
    def kill_h(self):
        self.__alive = False
    
    def check_h(self):
        if self.__eat < 0:
            print("{0} умер от голода".format(self.__name))
            self.__alive = False
        if self.__sleep < 0:
            print("{0} умер от изнеможения и недосыпа".format(self.__name))
            self.__alive = False
        if not(self.__alive):
            print("+_________+")
            print("|ПОТРАЧЕНО|")
            print("+_________+")
            print("{0} умер в возрасте {1} лет".format(self.__name, self.__age))
            print("И оставил в наследство {0} тысяч рублей".format(round(self.__money)))
            print("{0} был хорошим человеком: за жизнь пролистал {1} Двач-тредов".format(self.__name, self.__treads))
            print("Земля ему пуховик")
        return self.__alive

class Life:
    def life(self, human, years=70):
        while years:
            human.growing()
            human.eating(random.randint(0,4))
            human.sleeping(random.randint(0,4))
            human.working(random.randint(0,4))
            human.relaxing(random.randint(0,4))
            years -= 1
            if not(human.check_h()):
                break
        if years == 0:
            human.kill_h()
            human.check_h()

import random
petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)
